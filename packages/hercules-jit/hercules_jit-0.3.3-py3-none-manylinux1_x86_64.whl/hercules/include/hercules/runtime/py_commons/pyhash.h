// Copyright 2023 Hercules author.
/*
 * Acknowledgement: This file originates from CPython.
 * https://github.com/python/cpython/blob/3.8/Include/pyhash.h
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

#include <cstddef>

namespace hercules {
namespace runtime {
namespace py_builtins {

size_t _Py_HashDouble(double) noexcept;
size_t _Py_HashPointer(void*) noexcept;

// Replaced by Wyhash/CityHash64
// size_t _Py_HashBytes(const void* src, size_t len) noexcept;

}  // namespace py_builtins
}  // namespace runtime
}  // namespace hercules
