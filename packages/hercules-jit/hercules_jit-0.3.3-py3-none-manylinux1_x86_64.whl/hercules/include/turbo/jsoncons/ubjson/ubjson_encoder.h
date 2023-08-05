// Copyright 2013-2023 Daniel Parker
// Copyright 2023 The Turbo Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

#ifndef TURBO_JSONCONS_UBJSON_UBJSON_ENCODER_H_
#define TURBO_JSONCONS_UBJSON_UBJSON_ENCODER_H_

#include <string>
#include <vector>
#include <limits> // std::numeric_limits
#include <memory>
#include <utility> // std::move
#include "turbo/jsoncons/json_exception.h"
#include "turbo/jsoncons/json_visitor.h"
#include "turbo/jsoncons/config/jsoncons_config.h"
#include "turbo/jsoncons/sink.h"
#include "turbo/jsoncons/detail/parse_number.h"
#include "turbo/jsoncons/ubjson/ubjson_type.h"
#include "turbo/jsoncons/ubjson/ubjson_error.h"
#include "turbo/jsoncons/ubjson/ubjson_options.h"

namespace turbo::ubjson {

    enum class ubjson_container_type {
        object, indefinite_length_object, array, indefinite_length_array
    };

    template<class Sink=turbo::binary_stream_sink, class Allocator=std::allocator<char>>
    class basic_ubjson_encoder final : public basic_json_visitor<char> {

        enum class decimal_parse_state {
            start, integer, exp1, exp2, fraction1
        };
    public:
        using allocator_type = Allocator;
        using typename basic_json_visitor<char>::string_view_type;
        using sink_type = Sink;

    private:
        struct stack_item {
            ubjson_container_type type_;
            std::size_t length_;
            std::size_t count_;

            stack_item(ubjson_container_type type, std::size_t length = 0) noexcept
                    : type_(type), length_(length), count_(0) {
            }

            std::size_t length() const {
                return length_;
            }

            std::size_t count() const {
                return count_;
            }

            bool is_object() const {
                return type_ == ubjson_container_type::object ||
                       type_ == ubjson_container_type::indefinite_length_object;
            }

            bool is_indefinite_length() const {
                return type_ == ubjson_container_type::indefinite_length_array ||
                       type_ == ubjson_container_type::indefinite_length_object;
            }

        };

        Sink sink_;
        const ubjson_encode_options options_;
        allocator_type alloc_;

        std::vector<stack_item> stack_;
        int nesting_depth_;

        // Noncopyable and nonmoveable
        basic_ubjson_encoder(const basic_ubjson_encoder &) = delete;

        basic_ubjson_encoder &operator=(const basic_ubjson_encoder &) = delete;

    public:
        basic_ubjson_encoder(Sink &&sink,
                             const Allocator &alloc = Allocator())
                : basic_ubjson_encoder(std::forward<Sink>(sink), ubjson_encode_options(), alloc) {
        }

        explicit basic_ubjson_encoder(Sink &&sink,
                                      const ubjson_encode_options &options,
                                      const Allocator &alloc = Allocator())
                : sink_(std::forward<Sink>(sink)),
                  options_(options),
                  alloc_(alloc),
                  nesting_depth_(0) {
        }

        void reset() {
            stack_.clear();
            nesting_depth_ = 0;
        }

        void reset(Sink &&sink) {
            sink_ = std::move(sink);
            reset();
        }

        ~basic_ubjson_encoder() noexcept {
            JSONCONS_TRY {
                sink_.flush();
            }
            JSONCONS_CATCH(...) {
            }
        }

    private:
        // Implementing methods

        void visit_flush() override {
            sink_.flush();
        }

        bool visit_begin_object(semantic_tag, const ser_context &, std::error_code &ec) override {
            if (TURBO_UNLIKELY(++nesting_depth_ > options_.max_nesting_depth())) {
                ec = ubjson_errc::max_nesting_depth_exceeded;
                return false;
            }
            stack_.emplace_back(ubjson_container_type::indefinite_length_object);
            sink_.push_back(turbo::ubjson::ubjson_type::start_object_marker);

            return true;
        }

        bool
        visit_begin_object(std::size_t length, semantic_tag, const ser_context &, std::error_code &ec) override {
            if (TURBO_UNLIKELY(++nesting_depth_ > options_.max_nesting_depth())) {
                ec = ubjson_errc::max_nesting_depth_exceeded;
                return false;
            }
            stack_.emplace_back(ubjson_container_type::object, length);
            sink_.push_back(turbo::ubjson::ubjson_type::start_object_marker);
            sink_.push_back(turbo::ubjson::ubjson_type::count_marker);
            put_length(length);

            return true;
        }

        bool visit_end_object(const ser_context &, std::error_code &ec) override {
            TURBO_ASSERT(!stack_.empty());
            --nesting_depth_;

            if (stack_.back().is_indefinite_length()) {
                sink_.push_back(turbo::ubjson::ubjson_type::end_object_marker);
            } else {
                if (stack_.back().count() < stack_.back().length()) {
                    ec = ubjson_errc::too_few_items;
                    return false;
                }
                if (stack_.back().count() > stack_.back().length()) {
                    ec = ubjson_errc::too_many_items;
                    return false;
                }
            }
            stack_.pop_back();
            end_value();
            return true;
        }

        bool visit_begin_array(semantic_tag, const ser_context &, std::error_code &ec) override {
            if (TURBO_UNLIKELY(++nesting_depth_ > options_.max_nesting_depth())) {
                ec = ubjson_errc::max_nesting_depth_exceeded;
                return false;
            }
            stack_.emplace_back(ubjson_container_type::indefinite_length_array);
            sink_.push_back(turbo::ubjson::ubjson_type::start_array_marker);

            return true;
        }

        bool
        visit_begin_array(std::size_t length, semantic_tag, const ser_context &, std::error_code &ec) override {
            if (TURBO_UNLIKELY(++nesting_depth_ > options_.max_nesting_depth())) {
                ec = ubjson_errc::max_nesting_depth_exceeded;
                return false;
            }
            stack_.emplace_back(ubjson_container_type::array, length);
            sink_.push_back(turbo::ubjson::ubjson_type::start_array_marker);
            sink_.push_back(turbo::ubjson::ubjson_type::count_marker);
            put_length(length);

            return true;
        }

        bool visit_end_array(const ser_context &, std::error_code &ec) override {
            TURBO_ASSERT(!stack_.empty());
            --nesting_depth_;

            if (stack_.back().is_indefinite_length()) {
                sink_.push_back(turbo::ubjson::ubjson_type::end_array_marker);
            } else {
                if (stack_.back().count() < stack_.back().length()) {
                    ec = ubjson_errc::too_few_items;
                    return false;
                }
                if (stack_.back().count() > stack_.back().length()) {
                    ec = ubjson_errc::too_many_items;
                    return false;
                }
            }
            stack_.pop_back();
            end_value();
            return true;
        }

        bool visit_key(const string_view_type &name, const ser_context &, std::error_code &ec) override {
            auto sink = unicode_traits::validate(name.data(), name.size());
            if (sink.ec != unicode_traits::conv_errc()) {
                ec = ubjson_errc::invalid_utf8_text_string;
                return false;
            }

            put_length(name.length());

            for (auto c: name) {
                sink_.push_back(c);
            }
            return true;
        }

        bool visit_null(semantic_tag, const ser_context &, std::error_code &) override {
            // nil
            binary::native_to_big(static_cast<uint8_t>(turbo::ubjson::ubjson_type::null_type),
                                  std::back_inserter(sink_));
            end_value();
            return true;
        }

        bool visit_string(const string_view_type &sv, semantic_tag tag, const ser_context &,
                          std::error_code &ec) override {
            switch (tag) {
                case semantic_tag::bigint:
                case semantic_tag::bigdec: {
                    sink_.push_back(turbo::ubjson::ubjson_type::high_precision_number_type);
                    break;
                }
                default: {
                    sink_.push_back(turbo::ubjson::ubjson_type::string_type);
                    break;
                }
            }

            auto sink = unicode_traits::validate(sv.data(), sv.size());
            if (sink.ec != unicode_traits::conv_errc()) {
                ec = ubjson_errc::invalid_utf8_text_string;
                return false;
            }

            put_length(sv.length());

            for (auto c: sv) {
                sink_.push_back(c);
            }

            end_value();
            return true;
        }

        void put_length(std::size_t length) {
            if (length <= (std::numeric_limits<uint8_t>::max)()) {
                sink_.push_back(ubjson_type::uint8_type);
                binary::native_to_big(static_cast<uint8_t>(length), std::back_inserter(sink_));
            } else if (length <= (std::size_t) (std::numeric_limits<int16_t>::max)()) {
                sink_.push_back(ubjson_type::int16_type);
                binary::native_to_big(static_cast<uint16_t>(length), std::back_inserter(sink_));
            } else if (length <= (std::size_t) (std::numeric_limits<int32_t>::max)()) {
                sink_.push_back(ubjson_type::int32_type);
                binary::native_to_big(static_cast<uint32_t>(length), std::back_inserter(sink_));
            } else if (length <= (std::size_t) (std::numeric_limits<int64_t>::max)()) {
                sink_.push_back(ubjson_type::int64_type);
                binary::native_to_big(static_cast<uint64_t>(length), std::back_inserter(sink_));
            } else {
                JSONCONS_THROW(ser_error(ubjson_errc::too_many_items));
            }
        }

        bool visit_byte_string(const byte_string_view &b,
                               semantic_tag,
                               const ser_context &,
                               std::error_code &) override {

            const size_t length = b.size();
            sink_.push_back(turbo::ubjson::ubjson_type::start_array_marker);
            binary::native_to_big(static_cast<uint8_t>(turbo::ubjson::ubjson_type::type_marker),
                                  std::back_inserter(sink_));
            binary::native_to_big(static_cast<uint8_t>(turbo::ubjson::ubjson_type::uint8_type),
                                  std::back_inserter(sink_));
            put_length(length);

            for (auto c: b) {
                sink_.push_back(c);
            }

            end_value();
            return true;
        }

        bool visit_double(double val,
                          semantic_tag,
                          const ser_context &,
                          std::error_code &) override {
            float valf = (float) val;
            if ((double) valf == val) {
                // float 32
                sink_.push_back(static_cast<uint8_t>(turbo::ubjson::ubjson_type::float32_type));
                binary::native_to_big(valf, std::back_inserter(sink_));
            } else {
                // float 64
                sink_.push_back(static_cast<uint8_t>(turbo::ubjson::ubjson_type::float64_type));
                binary::native_to_big(val, std::back_inserter(sink_));
            }

            // write double

            end_value();
            return true;
        }

        bool visit_int64(int64_t val,
                         semantic_tag,
                         const ser_context &,
                         std::error_code &) override {
            if (val >= 0) {
                if (val <= (std::numeric_limits<uint8_t>::max)()) {
                    // uint 8 stores a 8-bit unsigned integer
                    sink_.push_back(turbo::ubjson::ubjson_type::uint8_type);
                    binary::native_to_big(static_cast<uint8_t>(val), std::back_inserter(sink_));
                } else if (val <= (std::numeric_limits<int16_t>::max)()) {
                    // uint 16 stores a 16-bit big-endian unsigned integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int16_type);
                    binary::native_to_big(static_cast<int16_t>(val), std::back_inserter(sink_));
                } else if (val <= (std::numeric_limits<int32_t>::max)()) {
                    // uint 32 stores a 32-bit big-endian unsigned integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int32_type);
                    binary::native_to_big(static_cast<int32_t>(val), std::back_inserter(sink_));
                } else if (val <= (std::numeric_limits<int64_t>::max)()) {
                    // int 64 stores a 64-bit big-endian signed integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int64_type);
                    binary::native_to_big(static_cast<int64_t>(val), std::back_inserter(sink_));
                } else {
                    // big integer
                }
            } else {
                if (val >= (std::numeric_limits<int8_t>::lowest)()) {
                    // int 8 stores a 8-bit signed integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int8_type);
                    binary::native_to_big(static_cast<int8_t>(val), std::back_inserter(sink_));
                } else if (val >= (std::numeric_limits<int16_t>::lowest)()) {
                    // int 16 stores a 16-bit big-endian signed integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int16_type);
                    binary::native_to_big(static_cast<int16_t>(val), std::back_inserter(sink_));
                } else if (val >= (std::numeric_limits<int32_t>::lowest)()) {
                    // int 32 stores a 32-bit big-endian signed integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int32_type);
                    binary::native_to_big(static_cast<int32_t>(val), std::back_inserter(sink_));
                } else if (val >= (std::numeric_limits<int64_t>::lowest)()) {
                    // int 64 stores a 64-bit big-endian signed integer
                    sink_.push_back(turbo::ubjson::ubjson_type::int64_type);
                    binary::native_to_big(static_cast<int64_t>(val), std::back_inserter(sink_));
                }
            }
            end_value();
            return true;
        }

        bool visit_uint64(uint64_t val,
                          semantic_tag,
                          const ser_context &,
                          std::error_code &) override {
            if (val <= (std::numeric_limits<uint8_t>::max)()) {
                sink_.push_back(turbo::ubjson::ubjson_type::uint8_type);
                binary::native_to_big(static_cast<uint8_t>(val), std::back_inserter(sink_));
            } else if (val <= static_cast<uint64_t>((std::numeric_limits<int16_t>::max)())) {
                sink_.push_back(turbo::ubjson::ubjson_type::int16_type);
                binary::native_to_big(static_cast<int16_t>(val), std::back_inserter(sink_));
            } else if (val <= static_cast<uint64_t>((std::numeric_limits<int32_t>::max)())) {
                sink_.push_back(turbo::ubjson::ubjson_type::int32_type);
                binary::native_to_big(static_cast<int32_t>(val), std::back_inserter(sink_));
            } else if (val <= static_cast<uint64_t>((std::numeric_limits<int64_t>::max)())) {
                sink_.push_back(turbo::ubjson::ubjson_type::int64_type);
                binary::native_to_big(static_cast<int64_t>(val), std::back_inserter(sink_));
            }
            end_value();
            return true;
        }

        bool visit_bool(bool val, semantic_tag, const ser_context &, std::error_code &) override {
            // true and false
            sink_.push_back(static_cast<uint8_t>(val ? turbo::ubjson::ubjson_type::true_type
                                                     : turbo::ubjson::ubjson_type::false_type));

            end_value();
            return true;
        }

        void end_value() {
            if (!stack_.empty()) {
                ++stack_.back().count_;
            }
        }
    };

    using ubjson_stream_encoder = basic_ubjson_encoder<turbo::binary_stream_sink>;
    using ubjson_bytes_encoder = basic_ubjson_encoder<turbo::bytes_sink<std::vector<uint8_t>>>;


}  // namespace turbo::ubjson

#endif  // TURBO_JSONCONS_UBJSON_UBJSON_ENCODER_H_

