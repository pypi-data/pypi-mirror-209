// Copyright 2020 The Turbo Authors.
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

#ifndef TURBO_STRINGS_INTERNAL_STR_FORMAT_CHECKER_H_
#define TURBO_STRINGS_INTERNAL_STR_FORMAT_CHECKER_H_

#include <algorithm>

#include "turbo/platform/port.h"
#include "turbo/strings/internal/str_format/arg.h"
#include "turbo/strings/internal/str_format/constexpr_parser.h"
#include "turbo/strings/internal/str_format/extension.h"

// Compile time check support for entry points.

#ifndef TURBO_INTERNAL_ENABLE_FORMAT_CHECKER
// We disable format checker under vscode intellisense compilation.
// See https://github.com/microsoft/vscode-cpptools/issues/3683 for
// more details.
#if TURBO_HAVE_ATTRIBUTE(enable_if) && !defined(__native_client__) && \
    !defined(__INTELLISENSE__)
#define TURBO_INTERNAL_ENABLE_FORMAT_CHECKER 1
#endif  // TURBO_HAVE_ATTRIBUTE(enable_if) && !defined(__native_client__) &&
        // !defined(__INTELLISENSE__)
#endif  // TURBO_INTERNAL_ENABLE_FORMAT_CHECKER

namespace turbo {
TURBO_NAMESPACE_BEGIN
namespace str_format_internal {

#ifdef TURBO_INTERNAL_ENABLE_FORMAT_CHECKER

template <FormatConversionCharSet... C>
constexpr bool ValidFormatImpl(std::string_view format) {
  int next_arg = 0;
  const char* p = format.data();
  const char* const end = p + format.size();
  constexpr FormatConversionCharSet
      kAllowedConvs[(std::max)(sizeof...(C), size_t{1})] = {C...};
  bool used[(std::max)(sizeof...(C), size_t{1})]{};
  constexpr int kNumArgs = sizeof...(C);
  while (p != end) {
    while (p != end && *p != '%') ++p;
    if (p == end) {
      break;
    }
    if (p + 1 >= end) return false;
    if (p[1] == '%') {
      // %%
      p += 2;
      continue;
    }

    UnboundConversion conv(turbo::kConstInit);
    p = ConsumeUnboundConversion(p + 1, end, &conv, &next_arg);
    if (p == nullptr) return false;
    if (conv.arg_position <= 0 || conv.arg_position > kNumArgs) {
      return false;
    }
    if (!Contains(kAllowedConvs[conv.arg_position - 1], conv.conv)) {
      return false;
    }
    used[conv.arg_position - 1] = true;
    for (auto extra : {conv.width, conv.precision}) {
      if (extra.is_from_arg()) {
        int pos = extra.get_from_arg();
        if (pos <= 0 || pos > kNumArgs) return false;
        used[pos - 1] = true;
        if (!Contains(kAllowedConvs[pos - 1], '*')) {
          return false;
        }
      }
    }
  }
  if (sizeof...(C) != 0) {
    for (bool b : used) {
      if (!b) return false;
    }
  }
  return true;
}

#endif  // TURBO_INTERNAL_ENABLE_FORMAT_CHECKER

}  // namespace str_format_internal
TURBO_NAMESPACE_END
}  // namespace turbo

#endif  // TURBO_STRINGS_INTERNAL_STR_FORMAT_CHECKER_H_
