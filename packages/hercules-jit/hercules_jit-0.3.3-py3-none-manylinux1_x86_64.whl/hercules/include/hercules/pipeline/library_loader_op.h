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

#include <hercules/pipeline/op_kernel.h>

namespace hercules {
namespace runtime {

class LibraryLoaderOp : public OpKernel {
 public:
  void Init() override;
  int Bundle(string_view folder) override;
  RTValue Process(PyArgs inputs) const override;

 private:
  void load_dl_paths(const List& dl_paths);

 private:
  List abi0_dl_paths_;
  List abi1_dl_paths_;
  std::vector<std::shared_ptr<void>> lib_holder_;
};

}  // namespace runtime
}  // namespace hercules