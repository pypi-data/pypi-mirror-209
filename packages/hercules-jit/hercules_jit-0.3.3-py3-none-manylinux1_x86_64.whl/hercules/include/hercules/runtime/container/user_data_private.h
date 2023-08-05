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

#include "./native_func_private.h"
#include "./native_object_private.h"
#include "./user_function_private.h"

#include <initializer_list>
#include <memory>
#include <type_traits>
#include <utility>
#include <vector>

#include <hercules/runtime/c_backend_api.h>
#include <hercules/runtime/container/_flat_hash_map.h>
#include <hercules/runtime/container/user_data_interface.h>
#include <hercules/runtime/func_registry_names_io.h>
#include <hercules/runtime/function_name_rules.h>
#include <hercules/runtime/logging.h>
#include <hercules/runtime/memory.h>
#include <hercules/runtime/object.h>
#include <hercules/runtime/py_args.h>
#include <hercules/runtime/runtime_value.h>

namespace hercules {
namespace runtime {

static void default_userdata_deleter(ILightUserData* self) {
  delete self;
}

/*! \brief An object representing a user data structure. */
struct UserDataNode : public Object {
  typedef void (*FUserDataDeleter)(ILightUserData* self);
  struct SafeDeleter {
    FUserDataDeleter deleter = default_userdata_deleter;
    ObjectRef module;
  };
  /*! \brief The tag representing the constructor used. */
  uint32_t tag;
  /*! \brief Number of member variable in the UserData object. */
  uint32_t var_num;
  /*! \brief UserData pointer. */
  ILightUserData* ud_ptr = nullptr;
  SafeDeleter safe_deleter;
  virtual ~UserDataNode() {
    if (safe_deleter.deleter && ud_ptr) {
      (*safe_deleter.deleter)(ud_ptr);
    }
  }

  virtual unsigned char* GetInternalBufferPtr() {
    return nullptr;
  }
  virtual size_t GetInternalBufferSize() const {
    return 0;
  }

  // get member var
  HERCULES_ALWAYS_INLINE RTView get_attr(string_view attr) const {
    return ud_ptr->__getattr__(attr);
  }

  // set member var
  HERCULES_ALWAYS_INLINE void set_attr(string_view attr, const Any& val) const {
    return ud_ptr->__setattr__(attr, val);
  }

  // get member var or method
  RTValue __getattr__(const string_view& attr) const;

  Unicode __str__() const;
  Unicode __repr__() const;

  // member var num
  HERCULES_ALWAYS_INLINE uint32_t size() const {
    return ud_ptr->size_2_71828182846();
  }

  ILightUserData* check_codegen_ptr(const char* expect_cls_name = "") const;
  uint32_t check_codegen_tag(const char* expect_cls_name = "") const;

  RTValue generic_call(PyArgs args);
  RTValue generic_call_attr(string_view func_name, PyArgs args);

  template <typename... ARGS>
  inline RTValue call(ARGS&&... args) {
    std::initializer_list<RTView> packed_args{std::forward<ARGS>(args)...};
    return generic_call(packed_args);
  }

  template <typename... ARGS>
  inline RTValue call_attr(string_view func_name, ARGS&&... args) {
    std::initializer_list<RTView> packed_args{std::forward<ARGS>(args)...};
    return generic_call_attr(func_name, packed_args);
  }

  static const UserDataNode* StripJitWrapper(const UserDataNode* node);

  static constexpr const uint32_t _type_index = TypeIndex::kRuntimeUserData;
  static constexpr const char* _type_key = "runtime.UserData";
  HERCULES_DECLARE_FINAL_OBJECT_INFO(UserDataNode, Object);
};

template <size_t BUFFER_SIZE>
struct UserDataNodeWithBuffer : public UserDataNode {
  unsigned char buffer[BUFFER_SIZE];
  unsigned char* GetInternalBufferPtr() override {
    return buffer;
  }
  size_t GetInternalBufferSize() const override {
    return BUFFER_SIZE;
  }

  ~UserDataNodeWithBuffer() override {
    if (safe_deleter.deleter && ud_ptr) {
      (*safe_deleter.deleter)(ud_ptr);
    }
    ud_ptr = nullptr;
    safe_deleter.deleter = nullptr;
  }
};

}  // namespace runtime
}  // namespace hercules
