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

#ifndef TURBO_UNICODE_SCALAR_VALID_UTF32_TO_UTF16_H_
#define TURBO_UNICODE_SCALAR_VALID_UTF32_TO_UTF16_H_

namespace turbo {
namespace scalar {
namespace {
namespace utf32_to_utf16 {

template <endianness big_endian>
inline size_t convert_valid(const char32_t* buf, size_t len, char16_t* utf16_output) {
  const uint32_t *data = reinterpret_cast<const uint32_t *>(buf);
  size_t pos = 0;
  char16_t* start{utf16_output};
  while (pos < len) {
    uint32_t word = data[pos];
    if((word & 0xFFFF0000)==0) {
      // will not generate a surrogate pair
      *utf16_output++ = !match_system(big_endian) ? char16_t(utf16::swap_bytes(uint16_t(word))) : char16_t(word);
      pos++;
    } else {
      // will generate a surrogate pair
      word -= 0x10000;
      uint16_t high_surrogate = uint16_t(0xD800 + (word >> 10));
      uint16_t low_surrogate = uint16_t(0xDC00 + (word & 0x3FF));
      if (!match_system(big_endian)) {
        high_surrogate = utf16::swap_bytes(high_surrogate);
        low_surrogate = utf16::swap_bytes(low_surrogate);
      }
      *utf16_output++ = char16_t(high_surrogate);
      *utf16_output++ = char16_t(low_surrogate);
      pos++;
    }
  }
  return utf16_output - start;
}

} // utf32_to_utf16 namespace
} // unnamed namespace
} // namespace scalar
} // namespace turbo

#endif  // TURBO_UNICODE_SCALAR_VALID_UTF32_TO_UTF16_H_
