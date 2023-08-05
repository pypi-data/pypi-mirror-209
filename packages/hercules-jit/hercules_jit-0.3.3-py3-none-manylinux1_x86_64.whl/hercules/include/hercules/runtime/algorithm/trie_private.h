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

#include "cedar.h"

#include <initializer_list>
#include <map>
#include <memory>
#include <type_traits>
#include <utility>
#include <vector>

#include <hercules/runtime/container/list_ref.h>
#include <hercules/runtime/container/string_view.h>
#include <hercules/runtime/container/tuple_ref.h>
#include <hercules/runtime/container/unicode_view.h>
#include <hercules/runtime/logging.h>
#include <hercules/runtime/memory.h>
#include <hercules/runtime/object.h>
#include <hercules/runtime/runtime_value.h>

namespace hercules {
namespace runtime {

class TrieNode : public Object {
#if defined(USE_CEDAR_UNORDERED)
  typedef cedar::da<int, -1, -2, false> cedar_t;
#else
  typedef cedar::da<int> cedar_t;
#endif
 public:
  explicit TrieNode(const std::map<string_view, int64_t>& dic);
  explicit TrieNode();

  // insert a <str, value> pair to trie
  void Update(const string_view& w, int64_t val = -1);
  void Update(const unicode_view& w, int64_t val = -1);

  // Finds the longest string in dic, which is a prefix of `w`.
  // Returns the UTF8 byte length of matched string.
  // `val` is set if a prefix match exists.
  // If no entry is found, return 0.
  int64_t PrefixSearch(const string_view& w, int64_t* val = nullptr) const;
  int64_t PrefixSearch(const unicode_view& w, int64_t* val = nullptr) const;
  std::vector<std::pair<int64_t, int64_t>> PrefixSearchAll(const string_view& w) const;
  std::vector<std::pair<int64_t, int64_t>> PrefixSearchAll(const unicode_view& w) const;

  // python
  void update(const string_view& w, int64_t val = -1);
  void update(const unicode_view& w, int64_t val = -1);
  void update(const Any& w, int64_t val = -1);
  Tuple prefix_search(const string_view& w, int64_t pos = 0) const;
  Tuple prefix_search(const unicode_view& w, int64_t pos = 0) const;
  Tuple prefix_search(const Any& w, int64_t pos = 0) const;
  List prefix_search_all(const string_view& w, int64_t pos = 0) const;
  List prefix_search_all(const unicode_view& w, int64_t pos = 0) const;
  List prefix_search_all(const Any& w, int64_t pos = 0) const;
  int save(const unicode_view& file_path) const;
  int load(const unicode_view& file_path) const;

  static constexpr const uint32_t _type_index = TypeIndex::kRuntimeTrie;
  static constexpr const char* _type_key = "runtime.Trie";
  HERCULES_DECLARE_FINAL_OBJECT_INFO(TrieNode, Object);

 private:
  std::unique_ptr<cedar_t> trie_;
  friend class Trie;
  friend class TrieNodeTrait;
};

}  // namespace runtime
}  // namespace hercules
