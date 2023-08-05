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

#ifndef TURBO_UNICODE_SCALAR_UTF32_H_
#define TURBO_UNICODE_SCALAR_UTF32_H_

namespace turbo {
namespace scalar {
namespace {
namespace utf32 {

inline TURBO_MUST_USE_RESULT bool validate(const char32_t *buf, size_t len) noexcept {
  const uint32_t *data = reinterpret_cast<const uint32_t *>(buf);
  uint64_t pos = 0;
  for(;pos < len; pos++) {
    uint32_t word = data[pos];
    if(word > 0x10FFFF || (word >= 0xD800 && word <= 0xDFFF)) {
        return false;
    }
  }
  return true;
}

inline TURBO_MUST_USE_RESULT result validate_with_errors(const char32_t *buf, size_t len) noexcept {
  const uint32_t *data = reinterpret_cast<const uint32_t *>(buf);
  size_t pos = 0;
  for(;pos < len; pos++) {
    uint32_t word = data[pos];
    if(word > 0x10FFFF) {
        return result(error_code::TOO_LARGE, pos);
    }
    if(word >= 0xD800 && word <= 0xDFFF) {
        return result(error_code::SURROGATE, pos);
    }
  }
  return result(error_code::SUCCESS, pos);
}

inline size_t Utf8LengthFromUtf32(const char32_t* buf, size_t len) {
  // We are not BOM aware.
  const uint32_t * p = reinterpret_cast<const uint32_t *>(buf);
  size_t counter{0};
  for(size_t i = 0; i < len; i++) {
    /** ASCII **/
    if(p[i] <= 0x7F) { counter++; }
    /** two-byte **/
    else if(p[i] <= 0x7FF) { counter += 2; }
    /** three-byte **/
    else if(p[i] <= 0xFFFF) { counter += 3; }
    /** four-bytes **/
    else { counter += 4; }
  }
  return counter;
}

inline size_t Utf16LengthFromUtf32(const char32_t* buf, size_t len) {
  // We are not BOM aware.
  const uint32_t * p = reinterpret_cast<const uint32_t *>(buf);
  size_t counter{0};
  for(size_t i = 0; i < len; i++) {
    /** non-surrogate word **/
    if(p[i] <= 0xFFFF) { counter++; }
    /** surrogate pair **/
    else { counter += 2; }
  }
  return counter;
}

} // utf32 namespace
} // unnamed namespace
} // namespace scalar
} // namespace turbo

#endif  // TURBO_UNICODE_SCALAR_UTF32_H_
