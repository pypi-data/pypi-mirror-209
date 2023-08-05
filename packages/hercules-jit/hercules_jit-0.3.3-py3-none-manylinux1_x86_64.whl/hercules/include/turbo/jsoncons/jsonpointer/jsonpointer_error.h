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

#ifndef JSONCONS_JSONPOINTER_JSONPOINTER_ERROR_HPP
#define JSONCONS_JSONPOINTER_JSONPOINTER_ERROR_HPP

#include "turbo/jsoncons/json_exception.h"
#include <system_error>

namespace turbo { namespace jsonpointer {

class jsonpointer_error : public std::system_error, public virtual json_exception
{
public:
    jsonpointer_error(const std::error_code& ec)
        : std::system_error(ec)
    {
    }
    jsonpointer_error(const std::error_code& ec, const std::string& what_arg)
        : std::system_error(ec, what_arg)
    {
    }
    jsonpointer_error(const std::error_code& ec, const char* what_arg)
        : std::system_error(ec, what_arg)
    {
    }
    jsonpointer_error(const jsonpointer_error& other) = default;

    jsonpointer_error(jsonpointer_error&& other) = default;

    const char* what() const noexcept override
    {
        return std::system_error::what();
    }
};

enum class jsonpointer_errc 
{
    success = 0,
    expected_slash = 1,
    index_exceeds_array_size,
    expected_0_or_1,
    invalid_index,
    key_not_found,
    key_already_exists,
    expected_object_or_array,
    end_of_input,
    unexpected_end_of_input,
    argument_to_unflatten_invalid,
    invalid_flattened_key,
    invalid_uri_escaped_data
};

class jsonpointer_error_category_impl
   : public std::error_category
{
public:
    const char* name() const noexcept override
    {
        return "jsoncons/jsonpointer";
    }
    std::string message(int ev) const override
    {
        switch (static_cast<jsonpointer_errc>(ev))
        {
            case jsonpointer_errc::expected_slash:
                return "Expected /";
            case jsonpointer_errc::index_exceeds_array_size:
                return "Index exceeds array size";
            case jsonpointer_errc::expected_0_or_1:
                return "Expected '0' or '1' after escape character '~'";
            case jsonpointer_errc::key_not_found:
                return "Key not found";
            case jsonpointer_errc::invalid_index:
                return "Invalid array index";
            case jsonpointer_errc::key_already_exists:
                return "Key already exists";
            case jsonpointer_errc::expected_object_or_array:
                return "Expected object or array";
            case jsonpointer_errc::end_of_input:
                return "Unexpected end of input";
            case jsonpointer_errc::unexpected_end_of_input:
                return "Unexpected end of jsonpointer input";
            case jsonpointer_errc::argument_to_unflatten_invalid:
                return "Argument to unflatten must be an object";
            case jsonpointer_errc::invalid_flattened_key:
                return "Flattened key is invalid";
            default:
                return "Unknown jsonpointer error";
        }
    }
};

inline
const std::error_category& jsonpointer_error_category()
{
  static jsonpointer_error_category_impl instance;
  return instance;
}

inline 
std::error_code make_error_code(jsonpointer_errc result)
{
    return std::error_code(static_cast<int>(result),jsonpointer_error_category());
}

}}

namespace std {
    template<>
    struct is_error_code_enum<turbo::jsonpointer::jsonpointer_errc> : public true_type
    {
    };
}

#endif
