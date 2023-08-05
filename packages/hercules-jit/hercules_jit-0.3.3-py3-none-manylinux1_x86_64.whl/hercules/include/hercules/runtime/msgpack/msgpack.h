// Copyright 2023 Hercules author.
/*
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

#include <hercules/runtime/container/string.h>
#include <hercules/runtime/container/string_view.h>
#include <hercules/runtime/runtime_value.h>

namespace hercules {
namespace runtime {
namespace serialization {

RTValue msgpack_loads(const string_view& s);

String msgpack_dumps(const Any& obj);

}  // namespace serialization
}  // namespace runtime
}  // namespace hercules
