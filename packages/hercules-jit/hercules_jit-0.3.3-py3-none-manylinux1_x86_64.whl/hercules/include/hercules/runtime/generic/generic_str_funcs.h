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

#include <hercules/runtime/c_runtime_api.h>
#include <hercules/runtime/container.h>
#include <hercules/runtime/ft_container.h>
#include <hercules/runtime/object.h>
#include <hercules/runtime/py_args.h>
#include <hercules/runtime/runtime_value.h>
#include <hercules/runtime/type_helper_macros.h>
#include <cstdint>

namespace hercules {
namespace runtime {

/******************************************************************************
 * string methods
 *****************************************************************************/

HERCULES_ALWAYS_INLINE auto kernel_str___len__(string_view self) {
  return self.size();
}
HERCULES_ALWAYS_INLINE auto kernel_str___getitem__(string_view self, int64_t index) {
  return StringHelper::GetItem(self, index);
}
HERCULES_ALWAYS_INLINE auto kernel_str___getslice__(string_view self,
                                                      int64_t start,
                                                      int64_t end) {
  return StringHelper::GetSlice(self, start, end);
}
HERCULES_ALWAYS_INLINE auto kernel_str___getslice__(string_view self,
                                                      int64_t start,
                                                      int64_t end,
                                                      int64_t step) {
  return StringHelper::GetSlice(self, start, end, step);
}

HERCULES_ALWAYS_INLINE auto kernel_str___contains__(string_view self, string_view item) {
  return StringHelper::Contains(self, item);
}

HERCULES_ALWAYS_INLINE auto kernel_str___contains__(string_view self, int64_t item) {
  return StringHelper::Contains(self, item);
}

HERCULES_ALWAYS_INLINE auto kernel_str___contains__(string_view self, const Any& item) {
  if (item.Is<string_view>()) {
    return StringHelper::Contains(self, item.AsNoCheck<string_view>());
  } else if (item.type_code() == TypeIndex::kRuntimeInteger) {
    return StringHelper::Contains(self, item.value().data.v_int64);
  } else {
    THROW_PY_TypeError("a bytes-like object is required, not '", item.type_name(), "'");
  }
  return false;
}

HERCULES_ALWAYS_INLINE auto kernel_str_lower(string_view self) {
  return StringHelper::Lower(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_upper(string_view self) {
  return StringHelper::Upper(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_isdigit(string_view self) {
  return StringHelper::Isdigit(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_isalpha(string_view self) {
  return StringHelper::Isalpha(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_decode(string_view self) {
  return StringHelper::Decode(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_split(string_view self,
                                               string_view sep = nullptr,
                                               int64_t maxsplit = -1) {
  return StringHelper::Split(self, sep, maxsplit);
}

HERCULES_ALWAYS_INLINE auto kernel_str_split(string_view self,
                                               const Any& sep,
                                               int64_t maxsplit = -1) {
  if (sep.is_nullptr()) {
    return StringHelper::Split(self, nullptr, maxsplit);
  } else {
    return StringHelper::Split(self, HERCULES_TYPE_AS(sep, string_view), maxsplit);
  }
}

template <typename T>
HERCULES_ALWAYS_INLINE auto kernel_str_split_ft(string_view self,
                                                  string_view sep = nullptr,
                                                  int64_t maxsplit = -1) {
  return StringHelper::SplitFT<T>(self, sep, maxsplit);
}

template <typename T>
HERCULES_ALWAYS_INLINE auto kernel_str_split_ft(string_view self,
                                                  const Any& sep,
                                                  int64_t maxsplit = -1) {
  if (sep.is_nullptr()) {
    return StringHelper::SplitFT<T>(self, nullptr, maxsplit);
  } else {
    return StringHelper::SplitFT<T>(self, HERCULES_TYPE_AS(sep, string_view), maxsplit);
  }
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_join(string_view self, Args&&... args) {
  return StringHelper::Join(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_replace(string_view self, Args&&... args) {
  return StringHelper::Replace(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_startswith(string_view self, Args&&... args) {
  return StringHelper::StartsWith(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_endswith(string_view self, Args&&... args) {
  return StringHelper::EndsWith(self, std::forward<Args>(args)...);
}

HERCULES_ALWAYS_INLINE auto kernel_str_lstrip(string_view self, string_view chars) {
  return StringHelper::LStrip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_str_lstrip(string_view self) {
  return StringHelper::LStrip(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_rstrip(string_view self, string_view chars) {
  return StringHelper::RStrip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_str_rstrip(string_view self) {
  return StringHelper::RStrip(self);
}

HERCULES_ALWAYS_INLINE auto kernel_str_strip(string_view self, string_view chars) {
  return StringHelper::Strip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_str_strip(string_view self) {
  return StringHelper::Strip(self);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_count(string_view self, Args&&... args) {
  return StringHelper::Count(self, std::forward<Args>(args)...);
}

HERCULES_ALWAYS_INLINE auto kernel_str_repeat(string_view self, int64_t times) {
  return StringHelper::Repeat(self, times);
}

/******************************************************************************
 * unicode methods
 *****************************************************************************/

HERCULES_ALWAYS_INLINE auto kernel_unicode___len__(unicode_view self) {
  return self.size();
}
HERCULES_ALWAYS_INLINE auto kernel_unicode___getitem__(unicode_view self, int64_t index) {
  return UnicodeHelper::GetItem(self, index);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode___getslice__(unicode_view self,
                                                          int64_t start,
                                                          int64_t end) {
  return UnicodeHelper::GetSlice(self, start, end, 1);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode___getslice__(unicode_view self,
                                                          int64_t start,
                                                          int64_t end,
                                                          int64_t step) {
  return UnicodeHelper::GetSlice(self, start, end, step);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode___contains__(unicode_view self, unicode_view item) {
  return UnicodeHelper::Contains(self, item);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_find(unicode_view self, Args&&... args) {
  return UnicodeHelper::PyFind(self, std::forward<Args>(args)...);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_lower(unicode_view self) {
  return UnicodeHelper::Lower(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_upper(unicode_view self) {
  return UnicodeHelper::Upper(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_isdigit(unicode_view self) {
  return UnicodeHelper::IsDigit(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_isalpha(unicode_view self) {
  return UnicodeHelper::IsAlpha(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_encode(unicode_view self) {
  return UnicodeHelper::Encode(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_split(unicode_view self,
                                                   unicode_view sep = nullptr,
                                                   int64_t maxsplit = -1) {
  return UnicodeHelper::Split(self, sep, maxsplit);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_split(unicode_view self,
                                                   const Any& sep,
                                                   int64_t maxsplit = -1) {
  if (sep.is_nullptr()) {
    return UnicodeHelper::Split(self, nullptr, maxsplit);
  } else {
    return UnicodeHelper::Split(self, HERCULES_TYPE_AS(sep, unicode_view), maxsplit);
  }
}

template <typename T>
HERCULES_ALWAYS_INLINE auto kernel_unicode_split_ft(unicode_view self,
                                                      unicode_view sep = nullptr,
                                                      int64_t maxsplit = -1) {
  return UnicodeHelper::SplitFT<T>(self, sep, maxsplit);
}

template <typename T>
HERCULES_ALWAYS_INLINE auto kernel_unicode_split_ft(unicode_view self,
                                                      const Any& sep,
                                                      int64_t maxsplit = -1) {
  if (sep.is_nullptr()) {
    return UnicodeHelper::SplitFT<T>(self, nullptr, maxsplit);
  } else {
    return UnicodeHelper::SplitFT<T>(self, HERCULES_TYPE_AS(sep, unicode_view), maxsplit);
  }
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_join(unicode_view self, Args&&... args) {
  return UnicodeHelper::Join(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_replace(unicode_view self, Args&&... args) {
  return UnicodeHelper::Replace(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_startswith(unicode_view self, Args&&... args) {
  return UnicodeHelper::StartsWith(self, std::forward<Args>(args)...);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_endswith(unicode_view self, Args&&... args) {
  return UnicodeHelper::EndsWith(self, std::forward<Args>(args)...);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_lstrip(unicode_view self, unicode_view chars) {
  return UnicodeHelper::LStrip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode_lstrip(unicode_view self) {
  return UnicodeHelper::LStrip(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_rstrip(unicode_view self, unicode_view chars) {
  return UnicodeHelper::RStrip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode_rstrip(unicode_view self) {
  return UnicodeHelper::RStrip(self);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_strip(unicode_view self, unicode_view chars) {
  return UnicodeHelper::Strip(self, chars);
}
HERCULES_ALWAYS_INLINE auto kernel_unicode_strip(unicode_view self) {
  return UnicodeHelper::Strip(self);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_count(unicode_view self, Args&&... args) {
  return UnicodeHelper::Count(self, std::forward<Args>(args)...);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_format(unicode_view self, PyArgs args) {
  return UnicodeHelper::Format(self, args);
}

HERCULES_ALWAYS_INLINE auto kernel_unicode_repeat(unicode_view self, int64_t times) {
  return UnicodeHelper::Repeat(self, times);
}

/******************************************************************************
 * fused str/bytes ops
 *****************************************************************************/
template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_str_fused_concat(Args&&... args) {
  GenericValueConverter<string_view> Converter;
  std::initializer_list<string_view> view_args{Converter(std::forward<Args>(args))...};
  return StringHelper::Concat(view_args);
}

template <typename... Args>
HERCULES_ALWAYS_INLINE auto kernel_unicode_fused_concat(Args&&... args) {
  GenericValueConverter<unicode_view> Converter;
  std::initializer_list<unicode_view> view_args{Converter(std::forward<Args>(args))...};
  return UnicodeHelper::Concat(view_args);
}

}  // namespace runtime
}  // namespace hercules
