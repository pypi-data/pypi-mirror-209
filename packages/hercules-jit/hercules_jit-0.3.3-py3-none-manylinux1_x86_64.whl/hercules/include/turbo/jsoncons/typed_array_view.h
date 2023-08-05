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

#ifndef JSONCONS_TYPED_ARRAY_VIEW_HPP
#define JSONCONS_TYPED_ARRAY_VIEW_HPP

#include <memory> // std::allocator
#include <string>
#include <stdexcept>
#include <system_error>
#include <ios>
#include <type_traits> // std::enable_if
#include <array> // std::array
#include <functional> // std::function
#include "turbo/jsoncons/json_exception.h"
#include "turbo/jsoncons/json_visitor.h"
#include "turbo/jsoncons/bigint.h"
#include "turbo/jsoncons/json_parser.h"
#include "turbo/jsoncons/ser_context.h"
#include "turbo/jsoncons/sink.h"
#include "turbo/jsoncons/detail/write_number.h"
#include "turbo/jsoncons/json_type_traits.h"
#include "turbo/jsoncons/value_converter.h"

namespace turbo {

    struct uint8_array_arg_t {explicit uint8_array_arg_t() = default; };
    constexpr uint8_array_arg_t uint8_array_arg = uint8_array_arg_t();
    struct uint16_array_arg_t {explicit uint16_array_arg_t() = default; };
    struct uint32_array_arg_t {explicit uint32_array_arg_t() = default; };
    constexpr uint32_array_arg_t uint32_array_arg = uint32_array_arg_t();
    struct uint64_array_arg_t {explicit uint64_array_arg_t() = default; };
    constexpr uint64_array_arg_t uint64_array_arg = uint64_array_arg_t();
    struct int8_array_arg_t {explicit int8_array_arg_t() = default; };
    constexpr int8_array_arg_t int8_array_arg = int8_array_arg_t();
    struct int16_array_arg_t {explicit int16_array_arg_t() = default; };
    constexpr int16_array_arg_t int16_array_arg = int16_array_arg_t();
    struct int32_array_arg_t {explicit int32_array_arg_t() = default; };
    constexpr int32_array_arg_t int32_array_arg = int32_array_arg_t();
    struct int64_array_arg_t {explicit int64_array_arg_t() = default; };
    constexpr int64_array_arg_t int64_array_arg = int64_array_arg_t();
    constexpr uint16_array_arg_t uint16_array_arg = uint16_array_arg_t();
    struct half_array_arg_t {explicit half_array_arg_t() = default; };
    constexpr half_array_arg_t half_array_arg = half_array_arg_t();
    struct float_array_arg_t {explicit float_array_arg_t() = default; };
    constexpr float_array_arg_t float_array_arg = float_array_arg_t();
    struct double_array_arg_t {explicit double_array_arg_t() = default; };
    constexpr double_array_arg_t double_array_arg = double_array_arg_t();
    struct float128_array_arg_t {explicit float128_array_arg_t() = default; };
    constexpr float128_array_arg_t float128_array_arg = float128_array_arg_t();

    enum class typed_array_type{uint8_value=1,uint16_value,uint32_value,uint64_value,
                                int8_value,int16_value,int32_value,int64_value, 
                                half_value, float_value,double_value};

    class typed_array_view
    {
        typed_array_type type_;
        union 
        {
            const uint8_t* uint8_data_;
            const uint16_t* uint16_data_;
            const uint32_t* uint32_data_;
            const uint64_t* uint64_data_;
            const int8_t* int8_data_;
            const int16_t* int16_data_;
            const int32_t* int32_data_;
            const int64_t* int64_data_;
            const float* float_data_;
            const double* double_data_;
        } data_;
        std::size_t size_;
    public:

        typed_array_view()
            : type_(), data_(), size_(0)
        {
        }

        typed_array_view(const typed_array_view& other)
            : type_(other.type_), data_(other.data_), size_(other.size())
        {
        }

        typed_array_view(typed_array_view&& other) noexcept
        {
            swap(*this,other);
        }

        typed_array_view(const uint8_t* data, std::size_t size)
            : type_(typed_array_type::uint8_value), size_(size)
        {
            data_.uint8_data_ = data;
        }

        typed_array_view(const uint16_t* data, std::size_t size)
            : type_(typed_array_type::uint16_value), size_(size)
        {
            data_.uint16_data_ = data;
        }

        typed_array_view(const uint32_t* data, std::size_t size)
            : type_(typed_array_type::uint32_value), size_(size)
        {
            data_.uint32_data_ = data;
        }

        typed_array_view(const uint64_t* data, std::size_t size)
            : type_(typed_array_type::uint64_value), size_(size)
        {
            data_.uint64_data_ = data;
        }

        typed_array_view(const int8_t* data, std::size_t size)
            : type_(typed_array_type::int8_value), size_(size)
        {
            data_.int8_data_ = data;
        }

        typed_array_view(const int16_t* data, std::size_t size)
            : type_(typed_array_type::int16_value), size_(size)
        {
            data_.int16_data_ = data;
        }

        typed_array_view(const int32_t* data, std::size_t size)
            : type_(typed_array_type::int32_value), size_(size)
        {
            data_.int32_data_ = data;
        }

        typed_array_view(const int64_t* data, std::size_t size)
            : type_(typed_array_type::int64_value), size_(size)
        {
            data_.int64_data_ = data;
        }

        typed_array_view(half_array_arg_t, const uint16_t* data, std::size_t size)
            : type_(typed_array_type::half_value), size_(size)
        {
            data_.uint16_data_ = data;
        }

        typed_array_view(const float* data, std::size_t size)
            : type_(typed_array_type::float_value), size_(size)
        {
            data_.float_data_ = data;
        }

        typed_array_view(const double* data, std::size_t size)
            : type_(typed_array_type::double_value), size_(size)
        {
            data_.double_data_ = data;
        }

        typed_array_view& operator=(const typed_array_view& other)
        {
            typed_array_view temp(other);
            swap(*this,temp);
            return *this;
        }

        typed_array_type type() const {return type_;}

        std::size_t size() const
        {
            return size_;
        }

        turbo::Span<const uint8_t> data(uint8_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::uint8_value);
            return turbo::Span<const uint8_t>(data_.uint8_data_, size_);
        }

        turbo::Span<const uint16_t> data(uint16_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::uint16_value);
            return turbo::Span<const uint16_t>(data_.uint16_data_, size_);
        }

        turbo::Span<const uint32_t> data(uint32_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::uint32_value);
            return turbo::Span<const uint32_t>(data_.uint32_data_, size_);
        }

        turbo::Span<const uint64_t> data(uint64_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::uint64_value);
            return turbo::Span<const uint64_t>(data_.uint64_data_, size_);
        }

        turbo::Span<const int8_t> data(int8_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::int8_value);
            return turbo::Span<const int8_t>(data_.int8_data_, size_);
        }

        turbo::Span<const int16_t> data(int16_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::int16_value);
            return turbo::Span<const int16_t>(data_.int16_data_, size_);
        }

        turbo::Span<const int32_t> data(int32_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::int32_value);
            return turbo::Span<const int32_t>(data_.int32_data_, size_);
        }

        turbo::Span<const int64_t> data(int64_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::int64_value);
            return turbo::Span<const int64_t>(data_.int64_data_, size_);
        }

        turbo::Span<const uint16_t> data(half_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::half_value);
            return turbo::Span<const uint16_t>(data_.uint16_data_, size_);
        }

        turbo::Span<const float> data(float_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::float_value);
            return turbo::Span<const float>(data_.float_data_, size_);
        }

        turbo::Span<const double> data(double_array_arg_t) const
        {
            TURBO_ASSERT(type_ == typed_array_type::double_value);
            return turbo::Span<const double>(data_.double_data_, size_);
        }

        friend void swap(typed_array_view& a, typed_array_view& b) noexcept
        {
            std::swap(a.data_,b.data_);
            std::swap(a.type_,b.type_);
            std::swap(a.size_,b.size_);
        }
    };

} // namespace turbo

#endif

