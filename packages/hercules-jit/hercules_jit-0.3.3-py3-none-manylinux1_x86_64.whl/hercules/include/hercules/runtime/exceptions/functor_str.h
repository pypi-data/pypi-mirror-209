// Copyright 2023 Hercules author.
/*
 * Acknowledgement: The structure of functor::str is inspired by pythran.
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

#include <sstream>
#include <string>

namespace hercules {
namespace runtime {
namespace builtins {
namespace functor {

template <class T>
inline std::string str(T const& t);

inline std::string str(bool b);
inline std::string str(int64_t value);
inline std::string str(double l);

template <class T>
inline std::string str(T const& t) {
  std::ostringstream oss;
  oss << t;
  return oss.str();
}

inline std::string str(bool b) {
  static char const repr[2][6] = {"False", "True\0"};
  return repr[b];
}

inline std::string str(int64_t value) {
  return std::to_string(value);
}

inline std::string str(double l) {
  // when using %g, only 6 significant bits are used, so this should be
  // enough.
  // Use snprintf though
  char buffer[8 * (1 << sizeof(l))];
  snprintf(buffer, sizeof(buffer), "%g", l);
  return buffer;
}

}  // namespace functor
}  // namespace builtins
}  // namespace runtime
}  // namespace hercules
