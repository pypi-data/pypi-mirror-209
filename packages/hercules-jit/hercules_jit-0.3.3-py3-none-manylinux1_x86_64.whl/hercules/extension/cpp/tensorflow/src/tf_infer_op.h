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

#include "hercules/runtime/runtime_value.h"
#include "tf_model.h"

#include <mutex>

#include "hercules/pipeline/op_kernel.h"

namespace hercules {
namespace runtime {

class TFInferOp : public OpKernel {
 public:
  struct Options {
    String model;
    int device = INT16_MIN;
  };

  void Init() override;
  RTValue Process(PyArgs inputs) const override;

 protected:
  Options options_;
  TFEnginePtr engine_;
};

}  // namespace runtime
}  // namespace hercules
