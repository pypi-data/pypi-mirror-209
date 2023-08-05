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

#ifndef TURBO_JSONCONS_JSON_DECODER_H_
#define TURBO_JSONCONS_JSON_DECODER_H_

#include <string>
#include <vector>
#include <type_traits> // std::true_type
#include <memory> // std::allocator
#include <iterator> // std::make_move_iterator
#include <utility> // std::move
#include "turbo/jsoncons/json_exception.h"
#include "turbo/jsoncons/json_visitor.h"
#include "turbo/jsoncons/json_object.h"

namespace turbo {

    template<class Json, class TempAllocator=std::allocator<char>>
    class json_decoder final : public basic_json_visitor<typename Json::char_type> {
    public:
        using char_type = typename Json::char_type;
        using typename basic_json_visitor<char_type>::string_view_type;

        using key_value_type = typename Json::key_value_type;
        using key_type = typename Json::key_type;
        using array = typename Json::array;
        using object = typename Json::object;
        using result_allocator_type = typename Json::allocator_type;
        using json_string_allocator = typename key_type::allocator_type;
        using json_array_allocator = typename array::allocator_type;
        using json_object_allocator = typename object::allocator_type;
        typedef typename std::allocator_traits<result_allocator_type>::template rebind_alloc<uint8_t> json_byte_allocator_type;
    private:

        enum class structure_type {
            root_t, array_t, object_t
        };

        struct structure_info {
            structure_type type_;
            std::size_t container_index_;

            structure_info(structure_type type, std::size_t offset) noexcept
                    : type_(type), container_index_(offset) {
            }

        };

        using temp_allocator_type = TempAllocator;
        typedef typename std::allocator_traits<temp_allocator_type>::template rebind_alloc<key_index_value<Json>> stack_item_allocator_type;
        typedef typename std::allocator_traits<temp_allocator_type>::template rebind_alloc<structure_info> structure_info_allocator_type;

        result_allocator_type result_allocator_;
        temp_allocator_type temp_allocator_;

        Json result_;

        std::size_t index_;
        key_type name_;
        std::vector<key_index_value<Json>, stack_item_allocator_type> item_stack_;
        std::vector<structure_info, structure_info_allocator_type> structure_stack_;
        bool is_valid_;

    public:
        json_decoder(const temp_allocator_type &temp_alloc = temp_allocator_type())
                : result_allocator_(result_allocator_type()),
                  temp_allocator_(temp_alloc),
                  result_(),
                  index_(0),
                  name_(result_allocator_),
                  item_stack_(temp_allocator_),
                  structure_stack_(temp_allocator_),
                  is_valid_(false) {
            item_stack_.reserve(1000);
            structure_stack_.reserve(100);
            structure_stack_.emplace_back(structure_type::root_t, 0);
        }

        json_decoder(result_allocator_arg_t,
                     const result_allocator_type &result_alloc)
                : result_allocator_(result_alloc),
                  temp_allocator_(),
                  result_(),
                  index_(0),
                  name_(result_allocator_),
                  item_stack_(),
                  structure_stack_(),
                  is_valid_(false) {
            item_stack_.reserve(1000);
            structure_stack_.reserve(100);
            structure_stack_.emplace_back(structure_type::root_t, 0);
        }

        json_decoder(result_allocator_arg_t,
                     const result_allocator_type &result_alloc,
                     const temp_allocator_type &temp_alloc)
                : result_allocator_(result_alloc),
                  temp_allocator_(temp_alloc),
                  result_(),
                  index_(0),
                  name_(result_allocator_),
                  item_stack_(temp_allocator_),
                  structure_stack_(temp_allocator_),
                  is_valid_(false) {
            item_stack_.reserve(1000);
            structure_stack_.reserve(100);
            structure_stack_.emplace_back(structure_type::root_t, 0);
        }

        void reset() {
            is_valid_ = false;
            index_ = 0;
            item_stack_.clear();
            structure_stack_.clear();
            structure_stack_.emplace_back(structure_type::root_t, 0);
        }

        bool is_valid() const {
            return is_valid_;
        }

        Json get_result() {
            TURBO_ASSERT(is_valid_);
            is_valid_ = false;
            return std::move(result_);
        }


    private:

        void visit_flush() override {
        }

        bool visit_begin_object(semantic_tag tag, const ser_context &, std::error_code &) override {
            if (structure_stack_.back().type_ == structure_type::root_t) {
                index_ = 0;
                item_stack_.clear();
                is_valid_ = false;
            }
            item_stack_.emplace_back(std::forward<key_type>(name_), index_++, json_object_arg, tag, result_allocator_);
            structure_stack_.emplace_back(structure_type::object_t, item_stack_.size() - 1);
            return true;
        }

        bool visit_end_object(const ser_context &, std::error_code &) override {
            TURBO_ASSERT(structure_stack_.size() > 0);
            TURBO_ASSERT(structure_stack_.back().type_ == structure_type::object_t);
            const size_t structure_index = structure_stack_.back().container_index_;
            TURBO_ASSERT(item_stack_.size() > structure_index);
            const size_t count = item_stack_.size() - (structure_index + 1);
            auto first = item_stack_.begin() + (structure_index + 1);

            if (count > 0) {
                item_stack_[structure_index].value.object_value().init(&item_stack_[structure_index + 1], count);
            }

            item_stack_.erase(first, item_stack_.end());
            structure_stack_.pop_back();
            if (structure_stack_.back().type_ == structure_type::root_t) {
                result_.swap(item_stack_.front().value);
                item_stack_.pop_back();
                is_valid_ = true;
                return false;
            }
            return true;
        }

        bool visit_begin_array(semantic_tag tag, const ser_context &, std::error_code &) override {
            if (structure_stack_.back().type_ == structure_type::root_t) {
                index_ = 0;
                item_stack_.clear();
                is_valid_ = false;
            }
            item_stack_.emplace_back(std::forward<key_type>(name_), index_++, json_array_arg, tag, result_allocator_);
            structure_stack_.emplace_back(structure_type::array_t, item_stack_.size() - 1);
            return true;
        }

        bool visit_end_array(const ser_context &, std::error_code &) override {
            TURBO_ASSERT(structure_stack_.size() > 1);
            TURBO_ASSERT(structure_stack_.back().type_ == structure_type::array_t);
            const size_t container_index = structure_stack_.back().container_index_;
            TURBO_ASSERT(item_stack_.size() > container_index);

            auto &container = item_stack_[container_index].value;

            const size_t size = item_stack_.size() - (container_index + 1);
            //std::cout << "size on item stack: " << size << "\n";

            if (size > 0) {
                container.reserve(size);
                auto first = item_stack_.begin() + (container_index + 1);
                auto last = first + size;
                for (auto it = first; it != last; ++it) {
                    container.push_back(std::move(it->value));
                }
                item_stack_.erase(first, item_stack_.end());
            }

            structure_stack_.pop_back();
            if (structure_stack_.back().type_ == structure_type::root_t) {
                result_.swap(item_stack_.front().value);
                item_stack_.pop_back();
                is_valid_ = true;
                return false;
            }
            return true;
        }

        bool visit_key(const string_view_type &name, const ser_context &, std::error_code &) override {
            name_ = key_type(name.data(), name.length(), result_allocator_);
            return true;
        }

        bool
        visit_string(const string_view_type &sv, semantic_tag tag, const ser_context &, std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, sv, tag, result_allocator_);
                    break;
                case structure_type::root_t:
                    result_ = Json(sv, tag, result_allocator_);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_byte_string(const byte_string_view &b,
                               semantic_tag tag,
                               const ser_context &,
                               std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, byte_string_arg, b, tag,
                                             result_allocator_);
                    break;
                case structure_type::root_t:
                    result_ = Json(byte_string_arg, b, tag, result_allocator_);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_byte_string(const byte_string_view &b,
                               uint64_t ext_tag,
                               const ser_context &,
                               std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, byte_string_arg, b, ext_tag,
                                             result_allocator_);
                    break;
                case structure_type::root_t:
                    result_ = Json(byte_string_arg, b, ext_tag, result_allocator_);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_int64(int64_t value,
                         semantic_tag tag,
                         const ser_context &,
                         std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, value, tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(value, tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_uint64(uint64_t value,
                          semantic_tag tag,
                          const ser_context &,
                          std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, value, tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(value, tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_half(uint16_t value,
                        semantic_tag tag,
                        const ser_context &,
                        std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, half_arg, value, tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(half_arg, value, tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_double(double value,
                          semantic_tag tag,
                          const ser_context &,
                          std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, value, tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(value, tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_bool(bool value, semantic_tag tag, const ser_context &, std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, value, tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(value, tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }

        bool visit_null(semantic_tag tag, const ser_context &, std::error_code &) override {
            switch (structure_stack_.back().type_) {
                case structure_type::object_t:
                case structure_type::array_t:
                    item_stack_.emplace_back(std::forward<key_type>(name_), index_++, null_type(), tag);
                    break;
                case structure_type::root_t:
                    result_ = Json(null_type(), tag);
                    is_valid_ = true;
                    return false;
            }
            return true;
        }
    };

} // namespace turbo

#endif  // TURBO_JSONCONS_JSON_DECODER_H_

