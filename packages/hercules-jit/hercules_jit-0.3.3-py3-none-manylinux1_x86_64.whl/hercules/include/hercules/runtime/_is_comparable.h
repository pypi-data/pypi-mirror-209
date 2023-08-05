// Copyright 2023 Hercules author.
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
#pragma once

#include <type_traits>

namespace hercules {
namespace runtime {
namespace {

template <class...>
using __my_void_t_for_comparable__ = void;

template <typename T, typename U, typename = __my_void_t_for_comparable__<>>
struct is_eq_comparable : std::false_type {};
template <typename T, typename U>
struct is_eq_comparable<
    T,
    U,
    __my_void_t_for_comparable__<decltype(std::declval<T&>() == std::declval<U&>(), void())>>
    : std::true_type {};

template <typename T, typename U, typename = __my_void_t_for_comparable__<>>
struct is_lt_comparable : std::false_type {};
template <typename T, typename U>
struct is_lt_comparable<
    T,
    U,
    __my_void_t_for_comparable__<decltype(std::declval<T&>() < std::declval<U&>(), void())>>
    : std::true_type {};

template <typename T, typename U, typename = __my_void_t_for_comparable__<>>
struct is_le_comparable : std::false_type {};
template <typename T, typename U>
struct is_le_comparable<
    T,
    U,
    __my_void_t_for_comparable__<decltype(std::declval<T&>() <= std::declval<U&>(), void())>>
    : std::true_type {};

template <typename T, typename U, typename = __my_void_t_for_comparable__<>>
struct is_gt_comparable : std::false_type {};
template <typename T, typename U>
struct is_gt_comparable<
    T,
    U,
    __my_void_t_for_comparable__<decltype(std::declval<T&>() > std::declval<U&>(), void())>>
    : std::true_type {};

template <typename T, typename U, typename = __my_void_t_for_comparable__<>>
struct is_ge_comparable : std::false_type {};
template <typename T, typename U>
struct is_ge_comparable<
    T,
    U,
    __my_void_t_for_comparable__<decltype(std::declval<T&>() >= std::declval<U&>(), void())>>
    : std::true_type {};

template <typename T, typename U>
struct is_comparable {
  static constexpr bool value = is_eq_comparable<T, U>::value && is_lt_comparable<T, U>::value &&
                                is_gt_comparable<T, U>::value;
};

}  // namespace
}  // namespace runtime
}  // namespace hercules
