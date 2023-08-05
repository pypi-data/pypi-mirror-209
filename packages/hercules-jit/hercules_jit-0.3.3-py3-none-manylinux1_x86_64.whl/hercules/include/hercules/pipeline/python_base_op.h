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

#include <map>
#include <vector>

#include <hercules/pipeline/op_kernel.h>

namespace hercules {
namespace runtime {

class PythonBaseOp : public OpKernel {
 public:
  void Init() override;

  RTValue Process(PyArgs inputs) const override;

 public:
  String py_op_name;     // py op name, for debug
  String pass_op_name;   // op class name, shouldn't be empty
  Dict pass_op_options;  // json, shouldn't be empty
  ska::flat_hash_map<String, std::vector<String>> sub_op_deps;
  NativeFunction py_callable;
};

}  // namespace runtime
}  // namespace hercules
