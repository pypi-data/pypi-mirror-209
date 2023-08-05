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

#pragma once

#include "turbo/unicode/utf.h"
#include <algorithm>
#include <string>
#include <list>
#include <iostream>


namespace turbo { namespace test {

  int main(int argc, char* argv[]);
  using test_procedure = void (*)(const turbo::Implementation& impl);
  struct test_entry {
    std::string name;
    test_procedure procedure;

    void operator()(const turbo::Implementation& impl) {
      procedure(impl);
    }
  };

  std::list<test_entry>& test_procedures();

  struct register_test {
    register_test(const char* name, test_procedure proc);
  };

}} // namespace namespace turbo::test


#define TEST(name)                                          \
void test_impl_##name(const turbo::Implementation& impl); \
void name(const turbo::Implementation& impl) {            \
  std::string title = #name;                                \
  std::replace(title.begin(), title.end(), '_', ' ');       \
  printf("%s...", title.c_str()); fflush(stdout);           \
  test_impl_##name(impl);                                   \
  puts(" OK");                                              \
}                                                           \
static turbo::test::register_test test_register_##name(#name, name); \
void test_impl_##name(const turbo::Implementation& implementation)

#define ASSERT_EQUAL(a, b) {                                      \
  const auto expr = (a);                                          \
  if (expr != b) {                                                \
    std::cout << "\nExpected " << expr << " to be " << b << ".\n";\
    printf("%s \n",#a);                                           \
    exit(1);                                                      \
  }                                                               \
}

#define ASSERT_TRUE(cond) {                                 \
  const bool expr = (cond);                                 \
  if (!expr) {                                              \
    printf("expected %s to be true, it's false\n", #cond);  \
    exit(1);                                                \
  }                                                         \
}

#define ASSERT_FALSE(cond) {                                \
  const bool expr = !(cond);                                \
  if (!expr) {                                              \
    printf("expected %s to be false, it's true\n", #cond);  \
    exit(1);                                                \
  }                                                         \
}
