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

#ifndef TURBO_UNICODE_WESTMERE_H_
#define TURBO_UNICODE_WESTMERE_H_

#ifdef TURBO_UNICODE_FALLBACK_H_
#error "westmere.h must be included before fallback.h"
#endif

#include "turbo/unicode/internal/config.h"

// Default Westmere to on if this is x86-64, unless we'll always select Haswell.
#ifndef TURBO_UNICODE_IMPLEMENTATION_WESTMERE
//
// You do not want to set it to (TURBO_PROCESSOR_X86_64 && !TURBO_UNICODE_REQUIRES_HASWELL)
// because you want to rely on runtime dispatch!
//
#if TURBO_UNICODE_CAN_ALWAYS_RUN_ICELAKE || TURBO_UNICODE_CAN_ALWAYS_RUN_HASWELL
#define TURBO_UNICODE_IMPLEMENTATION_WESTMERE 0
#elif defined(TURBO_PROCESSOR_X86_64)
#define TURBO_UNICODE_IMPLEMENTATION_WESTMERE 1
#else
#define TURBO_UNICODE_IMPLEMENTATION_WESTMERE 0
#endif

#endif

#if  TURBO_UNICODE_IMPLEMENTATION_WESTMERE && defined(TURBO_PROCESSOR_X86_64) && defined(__SSE4_2__) && defined(__PCLMUL__)
#define TURBO_UNICODE_CAN_ALWAYS_RUN_WESTMERE 1
#else
#define TURBO_UNICODE_CAN_ALWAYS_RUN_WESTMERE 0
#endif

#if TURBO_UNICODE_IMPLEMENTATION_WESTMERE

#define TURBO_UNICODE_TARGET_WESTMERE TURBO_TARGET_REGION("sse4.2,pclmul")

namespace turbo {
/**
 * Implementation for Westmere (Intel SSE4.2).
 */
namespace westmere {
} // namespace westmere
} // namespace turbo

//
// These two need to be included outside TURBO_TARGET_REGION
//
#include "turbo/unicode/westmere/implementation.h"
#include "turbo/unicode/westmere/intrinsics.h"

//
// The rest need to be inside the region
//
#include "turbo/unicode/westmere/begin.h"

// Declarations
#include "turbo/unicode/westmere/bitmanipulation.h"
#include "turbo/unicode/westmere/simd.h"

#include "turbo/unicode/westmere/end.h"

#endif // TURBO_UNICODE_IMPLEMENTATION_WESTMERE

#endif // TURBO_UNICODE_WESTMERE_H_
