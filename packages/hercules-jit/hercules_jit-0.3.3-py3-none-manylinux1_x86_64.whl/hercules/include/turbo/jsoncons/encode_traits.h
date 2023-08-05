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

#ifndef JSONCONS_ENCODE_TRAITS_HPP
#define JSONCONS_ENCODE_TRAITS_HPP

#include <string>
#include <tuple>
#include <array>
#include <memory>
#include <type_traits> // std::enable_if, std::true_type, std::false_type
#include "turbo/jsoncons/json_visitor.h"
#include "turbo/jsoncons/json_decoder.h"
#include "turbo/jsoncons/json_options.h"
#include "turbo/jsoncons/json_encoder.h"
#include "turbo/jsoncons/json_type_traits.h"
#include "turbo/jsoncons/conv_error.h"

namespace turbo {

    // encode_traits

    template <class T, class CharT, class Enable = void>
    struct encode_traits
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder,
                           const Json& proto, 
                           std::error_code& ec)
        {
            encode(std::integral_constant<bool, traits_extension::is_stateless<typename Json::allocator_type>::value>(),
                      val, encoder, proto, ec);
        }
    private:
        template <class Json>
        static void encode(std::true_type,
                           const T& val, 
                           basic_json_visitor<CharT>& encoder,
                           const Json& /*proto*/, 
                           std::error_code& ec)
        {
            auto j = json_type_traits<Json,T>::to_json(val);
            j.dump(encoder, ec);
        }
        template <class Json>
        static void encode(std::false_type, 
                           const T& val, 
                           basic_json_visitor<CharT>& encoder,
                           const Json& proto, 
                           std::error_code& ec)
        {
            auto j = json_type_traits<Json,T>::to_json(val, proto.get_allocator());
            j.dump(encoder, ec);
        }
    };

    // specializations

    // bool
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_bool<T>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            encoder.bool_value(val,semantic_tag::none,ser_context(),ec);
        }
    };

    // uint
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_u8_u16_u32_or_u64<T>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            encoder.uint64_value(val,semantic_tag::none,ser_context(),ec);
        }
    };

    // int
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_i8_i16_i32_or_i64<T>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            encoder.int64_value(val,semantic_tag::none,ser_context(),ec);
        }
    };

    // float or double
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_float_or_double<T>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            encoder.double_value(val,semantic_tag::none,ser_context(),ec);
        }
    };

    // string
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_string<T>::value &&
                                std::is_same<typename T::value_type,CharT>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            encoder.string_value(val,semantic_tag::none,ser_context(),ec);
        }
    };
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_string<T>::value &&
                                !std::is_same<typename T::value_type,CharT>::value 
    >::type>
    {
        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&, 
                           std::error_code& ec)
        {
            std::basic_string<CharT> s;
            unicode_traits::convert(val.data(), val.size(), s);
            encoder.string_value(s,semantic_tag::none,ser_context(),ec);
        }
    };

    // std::pair

    template <class T1, class T2, class CharT>
    struct encode_traits<std::pair<T1, T2>, CharT>
    {
        using value_type = std::pair<T1, T2>;

        template <class Json>
        static void encode(const value_type& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            encoder.begin_array(2,semantic_tag::none,ser_context(),ec);
            if (ec) return;
            encode_traits<T1,CharT>::encode(val.first, encoder, proto, ec);
            if (ec) return;
            encode_traits<T2,CharT>::encode(val.second, encoder, proto, ec);
            if (ec) return;
            encoder.end_array(ser_context(),ec);
        }
    };

    // std::tuple

    namespace detail
    {
        template<size_t Pos, std::size_t Size, class Json, class Tuple>
        struct json_serialize_tuple_helper
        {
            using char_type = typename Json::char_type;
            using element_type = typename std::tuple_element<Size-Pos, Tuple>::type;
            using next = json_serialize_tuple_helper<Pos-1, Size, Json, Tuple>;

            static void encode(const Tuple& tuple,
                               basic_json_visitor<char_type>& encoder, 
                               const Json& proto, 
                               std::error_code& ec)
            {
                encode_traits<element_type,char_type>::encode(std::get<Size-Pos>(tuple), encoder, proto, ec);
                if (ec) return;
                next::encode(tuple, encoder, proto, ec);
            }
        };

        template<size_t Size, class Json, class Tuple>
        struct json_serialize_tuple_helper<0, Size, Json, Tuple>
        {
            using char_type = typename Json::char_type;
            static void encode(const Tuple&,
                               basic_json_visitor<char_type>&, 
                               const Json&, 
                               std::error_code&)
            {
            }
        };
    } // namespace detail


    template <class CharT, typename... E>
    struct encode_traits<std::tuple<E...>, CharT>
    {
        using value_type = std::tuple<E...>;
        static constexpr std::size_t size = sizeof...(E);

        template <class Json>
        static void encode(const value_type& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            using helper = turbo::detail::json_serialize_tuple_helper<size, size, Json, std::tuple<E...>>;
            encoder.begin_array(size,semantic_tag::none,ser_context(),ec);
            if (ec) return;
            helper::encode(val, encoder, proto, ec);
            if (ec) return;
            encoder.end_array(ser_context(),ec);
        }
    };

    // vector like
    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 !traits_extension::is_typed_array<T>::value 
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            encoder.begin_array(val.size(),semantic_tag::none,ser_context(),ec);
            if (ec) return;
            for (auto it = std::begin(val); it != std::end(val); ++it)
            {
                encode_traits<value_type,CharT>::encode(*it, encoder, proto, ec);
                if (ec) return;
            }
            encoder.end_array(ser_context(), ec);
        }
    };

    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 traits_extension::is_typed_array<T>::value 
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json&,
                           std::error_code& ec)
        {
            encoder.typed_array(turbo::Span<const value_type>(val), semantic_tag::none, ser_context(), ec);
        }
    };

    // std::array

    template <class T, class CharT, std::size_t N>
    struct encode_traits<std::array<T,N>,CharT>
    {
        using value_type = typename std::array<T,N>::value_type;

        template <class Json>
        static void encode(const std::array<T, N>& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            encoder.begin_array(val.size(),semantic_tag::none,ser_context(),ec);
            if (ec) return;
            for (auto it = std::begin(val); it != std::end(val); ++it)
            {
                encode_traits<value_type,CharT>::encode(*it, encoder, proto, ec);
                if (ec) return;
            }
            encoder.end_array(ser_context(),ec);
        }
    };

    // map like

    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                                traits_extension::is_map_like<T>::value &&
                                traits_extension::is_constructible_from_const_pointer_and_size<typename T::key_type>::value
    >::type>
    {
        using mapped_type = typename T::mapped_type;
        using value_type = typename T::value_type;
        using key_type = typename T::key_type;

        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            encoder.begin_object(val.size(), semantic_tag::none, ser_context(), ec);
            if (ec) return;
            for (auto it = std::begin(val); it != std::end(val); ++it)
            {
                encoder.key(it->first);
                encode_traits<mapped_type,CharT>::encode(it->second, encoder, proto, ec);
                if (ec) return;
            }
            encoder.end_object(ser_context(), ec);
            if (ec) return;
        }
    };

    template <class T, class CharT>
    struct encode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                                traits_extension::is_map_like<T>::value &&
                                std::is_integral<typename T::key_type>::value
    >::type>
    {
        using mapped_type = typename T::mapped_type;
        using value_type = typename T::value_type;
        using key_type = typename T::key_type;

        template <class Json>
        static void encode(const T& val, 
                           basic_json_visitor<CharT>& encoder, 
                           const Json& proto, 
                           std::error_code& ec)
        {
            encoder.begin_object(val.size(), semantic_tag::none, ser_context(), ec);
            if (ec) return;
            for (auto it = std::begin(val); it != std::end(val); ++it)
            {
                std::basic_string<typename Json::char_type> s;
                turbo::detail::from_integer(it->first,s);
                encoder.key(s);
                encode_traits<mapped_type,CharT>::encode(it->second, encoder, proto, ec);
                if (ec) return;
            }
            encoder.end_object(ser_context(), ec);
            if (ec) return;
        }
    };

} // jsoncons

#endif

