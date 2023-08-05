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

#ifndef JSONCONS_DECODE_TRAITS_HPP
#define JSONCONS_DECODE_TRAITS_HPP

#include <string>
#include <tuple>
#include <array>
#include <memory>
#include <type_traits> // std::enable_if, std::true_type, std::false_type
#include "turbo/jsoncons/json_visitor.h"
#include "turbo/jsoncons/json_decoder.h"
#include "turbo/jsoncons/json_type_traits.h"
#include "turbo/jsoncons/staj_cursor.h"
#include "turbo/jsoncons/conv_error.h"
#include "turbo/jsoncons/traits_extension.h"

namespace turbo {

    // decode_traits

    template <class T, class CharT, class Enable = void>
    struct decode_traits
    {
        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>& decoder, 
                        std::error_code& ec)
        {
            decoder.reset();
            cursor.read_to(decoder, ec);
            if (ec)
            {
                JSONCONS_THROW(ser_error(ec, cursor.context().line(), cursor.context().column()));
            }
            else if (!decoder.is_valid())
            {
                JSONCONS_THROW(ser_error(conv_errc::conversion_failed, cursor.context().line(), cursor.context().column()));
            }
            return decoder.get_result().template as<T>();
        }
    };

    // specializations

    // primitive

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_primitive<T>::value
    >::type>
    {
        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>&, 
                        std::error_code& ec)
        {
            T v = cursor.current().template get<T>(ec);
            return v;
        }
    };

    // string

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_string<T>::value &&
                                std::is_same<typename T::value_type,CharT>::value
    >::type>
    {
        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>&, 
                        std::error_code& ec)
        {
            T v = cursor.current().template get<T>(ec);
            return v;
        }
    };

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<traits_extension::is_string<T>::value &&
                                !std::is_same<typename T::value_type,CharT>::value
    >::type>
    {
        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>&, 
                        std::error_code& ec)
        {
            auto val = cursor.current().template get<std::basic_string<CharT>>(ec);
            T s;
            if (!ec)
            {
                unicode_traits::convert(val.data(), val.size(), s);
            }
            return s;
        }
    };

    // std::pair

    template <class T1, class T2, class CharT>
    struct decode_traits<std::pair<T1, T2>, CharT>
    {
        template <class Json, class TempAllocator>
        static std::pair<T1, T2> decode(basic_staj_cursor<CharT>& cursor,
                                        json_decoder<Json, TempAllocator>& decoder,
                                        std::error_code& ec)
        {
            using value_type = std::pair<T1, T2>;
            cursor.array_expected(ec);
            if (ec)
            {
                return value_type{};
            }
            if (cursor.current().event_type() != staj_event_type::begin_array)
            {
                ec = conv_errc::not_pair;
                return value_type();
            }
            cursor.next(ec); // skip past array
            if (ec)
            {
                return value_type();
            }

            T1 v1 = decode_traits<T1,CharT>::decode(cursor, decoder, ec);
            if (ec) {return value_type();}
            cursor.next(ec);
            if (ec) {return value_type();}
            T2 v2 = decode_traits<T2, CharT>::decode(cursor, decoder, ec);
            if (ec) {return value_type();}
            cursor.next(ec);

            if (cursor.current().event_type() != staj_event_type::end_array)
            {
                ec = conv_errc::not_pair;
                return value_type();
            }
            return std::make_pair(v1, v2);
        }
    };

    // vector like
    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 traits_extension::is_back_insertable<T>::value &&
                 !traits_extension::is_typed_array<T>::value 
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>& decoder, 
                        std::error_code& ec)
        {
            T v;

            cursor.array_expected(ec);
            if (ec)
            {
                return T{};
            }
            if (cursor.current().event_type() != staj_event_type::begin_array)
            {
                ec = conv_errc::not_vector;
                return v;
            }
            cursor.next(ec);
            while (cursor.current().event_type() != staj_event_type::end_array && !ec)
            {
                v.push_back(decode_traits<value_type,CharT>::decode(cursor, decoder, ec));
                if (ec) {return T{};}
                cursor.next(ec);
            }
            return v;
        }
    };

    template <class T>
    struct typed_array_visitor : public default_json_visitor
    {
        T& v_;
        int level_;
    public:
        using value_type = typename T::value_type;

        typed_array_visitor(T& v)
            : default_json_visitor(false,conv_errc::not_vector), v_(v), level_(0)
        {
        }
    private:
        bool visit_begin_array(semantic_tag, 
                               const ser_context&, 
                               std::error_code& ec) override
        {      
            if (++level_ != 1)
            {
                ec = conv_errc::not_vector;
                return false;
            }
            return true;
        }

        bool visit_begin_array(std::size_t size, 
                            semantic_tag, 
                            const ser_context&, 
                            std::error_code& ec) override
        {
            if (++level_ != 1)
            {
                ec = conv_errc::not_vector;
                return false;
            }
            if (size > 0)
            {
                reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), v_, size);
            }
            return true;
        }

        bool visit_end_array(const ser_context&, 
                          std::error_code& ec) override
        {
            if (level_ != 1)
            {
                ec = conv_errc::not_vector;
                return false;
            }
            return false;
        }

        bool visit_uint64(uint64_t value, 
                             semantic_tag, 
                             const ser_context&,
                             std::error_code&) override
        {
            v_.push_back(static_cast<value_type>(value));
            return true;
        }

        bool visit_int64(int64_t value, 
                            semantic_tag,
                            const ser_context&,
                            std::error_code&) override
        {
            v_.push_back(static_cast<value_type>(value));
            return true;
        }

        bool visit_half(uint16_t value, 
                           semantic_tag,
                           const ser_context&,
                           std::error_code&) override
        {
            return visit_half_(typename std::integral_constant<bool, std::is_integral<value_type>::value>::type(), value);
        }

        bool visit_half_(std::true_type, uint16_t value)
        {
            v_.push_back(static_cast<value_type>(value));
            return true;
        }

        bool visit_half_(std::false_type, uint16_t value)
        {
            v_.push_back(static_cast<value_type>(binary::decode_half(value)));
            return true;
        }

        bool visit_double(double value, 
                             semantic_tag,
                             const ser_context&,
                             std::error_code&) override
        {
            v_.push_back(static_cast<value_type>(value));
            return true;
        }

        bool visit_typed_array(const turbo::Span<const value_type>& data,
                            semantic_tag,
                            const ser_context&,
                            std::error_code&) override
        {
            v_ = std::vector<value_type>(data.begin(),data.end());
            return false;
        }

        static
        void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static
        void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 traits_extension::is_back_insertable_byte_container<T>::value &&
                 traits_extension::is_typed_array<T>::value
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>&, 
                        std::error_code& ec)
        {
            cursor.array_expected(ec);
            if (ec)
            {
                return T{};
            }
            switch (cursor.current().event_type())
            {
                case staj_event_type::byte_string_value:
                {
                    auto bytes = cursor.current().template get<byte_string_view>(ec);
                    if (!ec) 
                    {
                        T v;
                        if (cursor.current().size() > 0)
                        {
                            reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), v, cursor.current().size());
                        }
                        for (auto ch : bytes)
                        {
                            v.push_back(static_cast<value_type>(ch));
                        }
                        cursor.next(ec);
                        return v;
                    }
                    else
                    {
                        return T{};
                    }
                }
                case staj_event_type::begin_array:
                {
                    T v;
                    if (cursor.current().size() > 0)
                    {
                        reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), v, cursor.current().size());
                    }
                    typed_array_visitor<T> visitor(v);
                    cursor.read_to(visitor, ec);
                    return v;
                }
                default:
                {
                    ec = conv_errc::not_vector;
                    return T{};
                }
            }
        }

        static void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 traits_extension::is_back_insertable<T>::value &&
                 !traits_extension::is_back_insertable_byte_container<T>::value &&
                 traits_extension::is_typed_array<T>::value
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>&, 
                        std::error_code& ec)
        {
            cursor.array_expected(ec);
            if (ec)
            {
                return T{};
            }
            switch (cursor.current().event_type())
            {
                case staj_event_type::begin_array:
                {
                    T v;
                    if (cursor.current().size() > 0)
                    {
                        reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), v, cursor.current().size());
                    }
                    typed_array_visitor<T> visitor(v);
                    cursor.read_to(visitor, ec);
                    return v;
                }
                default:
                {
                    ec = conv_errc::not_vector;
                    return T{};
                }
            }
        }

        static void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

    // set like
    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                 traits_extension::is_list_like<T>::value &&
                 !traits_extension::is_back_insertable<T>::value &&
                 traits_extension::is_insertable<T>::value 
    >::type>
    {
        using value_type = typename T::value_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>& decoder, 
                        std::error_code& ec)
        {
            T v;

            cursor.array_expected(ec);
            if (ec)
            {
                return T{};
            }
            if (cursor.current().event_type() != staj_event_type::begin_array)
            {
                ec = conv_errc::not_vector;
                return v;
            }
            if (cursor.current().size() > 0)
            {
                reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), v, cursor.current().size());
            }
            cursor.next(ec);
            while (cursor.current().event_type() != staj_event_type::end_array && !ec)
            {
                v.insert(decode_traits<value_type,CharT>::decode(cursor, decoder, ec));
                if (ec) {return T{};}
                cursor.next(ec);
                if (ec) {return T{};}
            }
            return v;
        }

        static void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

    // std::array

    template <class T, class CharT, std::size_t N>
    struct decode_traits<std::array<T,N>,CharT>
    {
        using value_type = typename std::array<T,N>::value_type;

        template <class Json,class TempAllocator>
        static std::array<T, N> decode(basic_staj_cursor<CharT>& cursor, 
                                       json_decoder<Json,TempAllocator>& decoder, 
                                       std::error_code& ec)
        {
            std::array<T,N> v;
            cursor.array_expected(ec);
            if (ec)
            {
                v.fill(T());
                return v;
            }
            v.fill(T{});
            if (cursor.current().event_type() != staj_event_type::begin_array)
            {
                ec = conv_errc::not_vector;
                return v;
            }
            cursor.next(ec);
            for (std::size_t i = 0; i < N && cursor.current().event_type() != staj_event_type::end_array && !ec; ++i)
            {
                v[i] = decode_traits<value_type,CharT>::decode(cursor, decoder, ec);
                if (ec) {return v;}
                cursor.next(ec);
                if (ec) {return v;}
            }
            return v;
        }
    };

    // map like

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                                traits_extension::is_map_like<T>::value &&
                                traits_extension::is_constructible_from_const_pointer_and_size<typename T::key_type>::value
    >::type>
    {
        using mapped_type = typename T::mapped_type;
        using value_type = typename T::value_type;
        using key_type = typename T::key_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>& decoder, 
                        std::error_code& ec)
        {
            T val;
            if (cursor.current().event_type() != staj_event_type::begin_object)
            {
                ec = conv_errc::not_map;
                return val;
            }
            if (cursor.current().size() > 0)
            {
                reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), val, cursor.current().size());
            }
            cursor.next(ec);

            while (cursor.current().event_type() != staj_event_type::end_object && !ec)
            {
                if (cursor.current().event_type() != staj_event_type::key)
                {
                    ec = json_errc::expected_key;
                    return val;
                }
                auto key = cursor.current().template get<key_type>(ec);
                if (ec) return val;
                cursor.next(ec);
                if (ec) return val;
                val.emplace(std::move(key),decode_traits<mapped_type,CharT>::decode(cursor, decoder, ec));
                if (ec) {return val;}
                cursor.next(ec);
                if (ec) {return val;}
            }
            return val;
        }

        static void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

    template <class T, class CharT>
    struct decode_traits<T,CharT,
        typename std::enable_if<!is_json_type_traits_declared<T>::value && 
                                traits_extension::is_map_like<T>::value &&
                                std::is_integral<typename T::key_type>::value
    >::type>
    {
        using mapped_type = typename T::mapped_type;
        using value_type = typename T::value_type;
        using key_type = typename T::key_type;

        template <class Json,class TempAllocator>
        static T decode(basic_staj_cursor<CharT>& cursor, 
                        json_decoder<Json,TempAllocator>& decoder, 
                        std::error_code& ec)
        {
            T val;
            if (cursor.current().event_type() != staj_event_type::begin_object)
            {
                ec = conv_errc::not_map;
                return val;
            }
            if (cursor.current().size() > 0)
            {
                reserve_storage(typename std::integral_constant<bool, traits_extension::has_reserve<T>::value>::type(), val, cursor.current().size());
            }
            cursor.next(ec);

            while (cursor.current().event_type() != staj_event_type::end_object && !ec)
            {
                if (cursor.current().event_type() != staj_event_type::key)
                {
                    ec = json_errc::expected_key;
                    return val;
                }
                auto s = cursor.current().template get<turbo::basic_string_view<typename Json::char_type>>(ec);
                if (ec) return val;
                key_type n{0};
                auto r = turbo::detail::to_integer(s.data(), s.size(), n);
                if (r.ec != turbo::detail::to_integer_errc())
                {
                    ec = json_errc::invalid_number;
                    return val;
                }
                cursor.next(ec);
                if (ec) return val;
                val.emplace(n, decode_traits<mapped_type,CharT>::decode(cursor, decoder, ec));
                if (ec) {return val;}
                cursor.next(ec);
                if (ec) {return val;}
            }
            return val;
        }

        static void reserve_storage(std::true_type, T& v, std::size_t new_cap)
        {
            v.reserve(new_cap);
        }

        static void reserve_storage(std::false_type, T&, std::size_t)
        {
        }
    };

} // jsoncons

#endif

