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

#ifndef TURBO_UNICODE_WESTMERE_BITMANIPULATION_H_
#define TURBO_UNICODE_WESTMERE_BITMANIPULATION_H_

namespace turbo {
namespace TURBO_UNICODE_IMPLEMENTATION {
namespace {

#ifdef _MSC_VER
TURBO_FORCE_INLINE unsigned __int64 count_ones(uint64_t input_num) {
  // note: we do not support legacy 32-bit Windows
  return __popcnt64(input_num);// Visual Studio wants two underscores
}
#else
TURBO_FORCE_INLINE long long int count_ones(uint64_t input_num) {
  return _popcnt64(input_num);
}
#endif

} // unnamed namespace
} // namespace TURBO_UNICODE_IMPLEMENTATION
} // namespace turbo

#endif // TURBO_UNICODE_WESTMERE_BITMANIPULATION_H_
