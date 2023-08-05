// Copyright 2023 Hercules author.
/*
 * Acknowledgement: This file originates from CPython.
 *
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

#include <hercules/runtime/container/string_view.h>
#include <hercules/runtime/runtime_port.h>

namespace hercules {
namespace runtime {

namespace UnicodeNormalForm {

static constexpr int Invalid = -1;
static constexpr int NFC = 0;
static constexpr int NFKC = 1;
static constexpr int NFD = 2;
static constexpr int NFKD = 3;

HERCULES_DLL int32_t FromStr(string_view form) noexcept;
HERCULES_DLL string_view ToStr(int32_t form) noexcept;

}  // namespace UnicodeNormalForm

}  // namespace runtime
}  // namespace hercules
