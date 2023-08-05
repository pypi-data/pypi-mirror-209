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

#include "turbo/unicode/scalar/utf16.h"
namespace turbo {
namespace TURBO_UNICODE_IMPLEMENTATION {
namespace {
namespace utf16 {

template <endianness big_endian>
TURBO_FORCE_INLINE size_t count_code_points(const char16_t* in, size_t size) {
    size_t pos = 0;
    size_t count = 0;
    for(;pos + 32 <= size; pos += 32) {
      simd16x32<uint16_t> input(reinterpret_cast<const uint16_t *>(in + pos));
      if (!match_system(big_endian)) input.swap_bytes();
      uint64_t not_pair = input.not_in_range(0xDC00, 0xDFFF);
      count += count_ones(not_pair) / 2;
    }
    return count + scalar::utf16::count_code_points<big_endian>(in + pos, size - pos);
}

template <endianness big_endian>
TURBO_FORCE_INLINE size_t Utf8LengthFromUtf16(const char16_t* in, size_t size) {
    size_t pos = 0;
    size_t count = 0;
    // This algorithm could no doubt be improved!
    for(;pos + 32 <= size; pos += 32) {
      simd16x32<uint16_t> input(reinterpret_cast<const uint16_t *>(in + pos));
      if (!match_system(big_endian)) input.swap_bytes();
      uint64_t ascii_mask = input.lteq(0x7F);
      uint64_t twobyte_mask = input.lteq(0x7FF);
      uint64_t not_pair_mask = input.not_in_range(0xD800, 0xDFFF);

      size_t ascii_count = count_ones(ascii_mask) / 2;
      size_t twobyte_count = count_ones(twobyte_mask & ~ ascii_mask) / 2;
      size_t threebyte_count = count_ones(not_pair_mask & ~ twobyte_mask) / 2;
      size_t fourbyte_count = 32 - count_ones(not_pair_mask) / 2;
      count += 2 * fourbyte_count + 3 * threebyte_count + 2 * twobyte_count + ascii_count;
    }
    return count + scalar::utf16::Utf8LengthFromUtf16<big_endian>(in + pos, size - pos);
}

template <endianness big_endian>
TURBO_FORCE_INLINE size_t Utf32LengthFromUtf16(const char16_t* in, size_t size) {
    return count_code_points<big_endian>(in, size);
}

TURBO_FORCE_INLINE void ChangeEndiannessUtf16(const char16_t* in, size_t size, char16_t* output) {
  size_t pos = 0;

  while (pos + 32 <= size) {
    simd16x32<uint16_t> input(reinterpret_cast<const uint16_t *>(in + pos));
    input.swap_bytes();
    input.store(reinterpret_cast<uint16_t *>(output));
    pos += 32;
    output += 32;
  }

  scalar::utf16::ChangeEndiannessUtf16(in + pos, size - pos, output);
}

} // utf16
} // unnamed namespace
} // namespace TURBO_UNICODE_IMPLEMENTATION
} // namespace turbo
