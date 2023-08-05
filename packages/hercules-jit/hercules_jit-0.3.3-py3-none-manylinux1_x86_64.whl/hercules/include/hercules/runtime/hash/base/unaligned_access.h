// Copyright 2023 Hercules author.
// Taken from https://github.com/abseil/abseil-cpp/blob/master/absl/base/internal/unaligned_access.h
//
// Copyright 2017 The Abseil Authors.
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

#pragma once

#include <string.h>
#include <cstdint>

// unaligned APIs
// Portable handling of unaligned loads, stores, and copies.

// The unaligned API is C++ only.  The declarations use C++ features
// (namespaces, inline) which are absent or incompatible in C.
#if defined(__cplusplus)
namespace hercules {
namespace runtime {
namespace base_internal {

inline uint16_t UnalignedLoad16(const void* p) noexcept {
  uint16_t t;
  memcpy(&t, p, sizeof t);
  return t;
}

inline uint32_t UnalignedLoad32(const void* p) noexcept {
  uint32_t t;
  memcpy(&t, p, sizeof t);
  return t;
}

inline uint64_t UnalignedLoad64(const void* p) noexcept {
  uint64_t t;
  memcpy(&t, p, sizeof t);
  return t;
}

inline void UnalignedStore16(void* p, uint16_t v) noexcept {
  memcpy(p, &v, sizeof v);
}

inline void UnalignedStore32(void* p, uint32_t v) noexcept {
  memcpy(p, &v, sizeof v);
}

inline void UnalignedStore64(void* p, uint64_t v) noexcept {
  memcpy(p, &v, sizeof v);
}

}  // namespace base_internal
}  // namespace runtime
}  // namespace hercules

#define HERCULES_INTERNAL_UNALIGNED_LOAD16(_p) (base_internal::UnalignedLoad16(_p))
#define HERCULES_INTERNAL_UNALIGNED_LOAD32(_p) (base_internal::UnalignedLoad32(_p))
#define HERCULES_INTERNAL_UNALIGNED_LOAD64(_p) (base_internal::UnalignedLoad64(_p))

#define HERCULES_INTERNAL_UNALIGNED_STORE16(_p, _val) (base_internal::UnalignedStore16(_p, _val))
#define HERCULES_INTERNAL_UNALIGNED_STORE32(_p, _val) (base_internal::UnalignedStore32(_p, _val))
#define HERCULES_INTERNAL_UNALIGNED_STORE64(_p, _val) (base_internal::UnalignedStore64(_p, _val))

#endif  // defined(__cplusplus), end of unaligned API