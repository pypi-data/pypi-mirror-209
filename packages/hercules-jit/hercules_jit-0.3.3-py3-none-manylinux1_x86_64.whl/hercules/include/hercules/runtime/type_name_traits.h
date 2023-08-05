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
#include <typeindex>

#include <hercules/runtime/container/_flat_hash_map.h>
#include <hercules/runtime/container/string_view.h>

namespace hercules {
namespace runtime {

struct TypeNameTraits {
  HERCULES_DLL static TypeNameTraits& Register(std::type_index ty_idx, string_view name);
  HERCULES_DLL static string_view Get(std::type_index ty_idx);

  template <class T>
  inline static TypeNameTraits& Register(string_view name) {
    return Register(typeid(T), name);
  }
  template <class T>
  inline static string_view Get() {
    return Get(typeid(T));
  }

 private:
  // Internal class.
  struct Manager;
  TypeNameTraits() = default;
  ~TypeNameTraits() = default;
  ska::flat_hash_map<std::type_index, string_view> type_info_;
  friend struct Manager;
};

#define HERCULES_TYPE_NAME_TRAITS_VAR_DEF(T) \
  static HERCULES_ATTRIBUTE_UNUSED auto& __make_##HERCULES_TYPE_TRAITS##T

#define HERCULES_REGISTER_TYPE_NAME_TRAITS(T)                                \
  HERCULES_STR_CONCAT(HERCULES_TYPE_NAME_TRAITS_VAR_DEF(T), __COUNTER__) = \
      ::hercules::runtime::TypeNameTraits::Register<T>(#T)

}  // namespace runtime
}  // namespace hercules
