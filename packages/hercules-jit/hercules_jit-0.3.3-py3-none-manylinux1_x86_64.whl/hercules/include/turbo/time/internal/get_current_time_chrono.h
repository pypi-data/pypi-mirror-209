// Copyright 2018 The Turbo Authors.
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

#include <chrono>
#include <cstdint>

namespace turbo {
TURBO_NAMESPACE_BEGIN
namespace time_internal {

static int64_t GetCurrentTimeNanosFromSystem() {
  return std::chrono::duration_cast<std::chrono::nanoseconds>(
             std::chrono::system_clock::now() -
             std::chrono::system_clock::from_time_t(0))
      .count();
}

}  // namespace time_internal
TURBO_NAMESPACE_END
}  // namespace turbo
