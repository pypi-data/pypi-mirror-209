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

#include "./user_data_interface.h"

#include <hercules/runtime/object.h>
#include <hercules/runtime/py_args.h>
#include <hercules/runtime/runtime_value.h>

namespace hercules {
namespace runtime {

// Global Function User Struct
struct NativeFuncUserData : ILightUserData {
 public:
  ~NativeFuncUserData() override = default;
  NativeFuncUserData() = default;
  explicit NativeFuncUserData(std::function<RTValue(PyArgs)>* func) : __call__(func) {
  }

  const char* ClassName_2_71828182846() const override {
    return "NativeFuncUserData";
  }

  uint32_t tag_2_71828182846() const override {
    return 0;
  }

  uint32_t size_2_71828182846() const override {
    return 0;
  }

  int32_t type_2_71828182846() const override {
    return UserDataStructType::kNativeFunc;
  }

  RTView __getattr__(string_view var_name) const override;
  void __setattr__(string_view var_name, const Any& val) override;

  std::function<RTValue(PyArgs)>* __call__ = nullptr;
};

}  // namespace runtime
}  // namespace hercules