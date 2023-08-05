// Copyright 2013-2023 Daniel Parker
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
//

#ifndef TURBO_JSONCONS_CBOR_CBOR_OPTIONS_H_
#define TURBO_JSONCONS_CBOR_CBOR_OPTIONS_H_

#include <string>
#include <limits> // std::numeric_limits
#include <cwchar>
#include "turbo/jsoncons/json_exception.h"
#include "turbo/jsoncons/cbor/cbor_detail.h"

namespace turbo {
    namespace cbor {

        class cbor_options;

        class cbor_options_common {
            friend class cbor_options;

            int max_nesting_depth_;
        protected:
            virtual ~cbor_options_common() = default;

            cbor_options_common()
                    : max_nesting_depth_(1024) {
            }

            cbor_options_common(const cbor_options_common &) = default;

            cbor_options_common &operator=(const cbor_options_common &) = default;

            cbor_options_common(cbor_options_common &&) = default;

            cbor_options_common &operator=(cbor_options_common &&) = default;

        public:
            int max_nesting_depth() const {
                return max_nesting_depth_;
            }
        };

        class cbor_decode_options : public virtual cbor_options_common {
            friend class cbor_options;

        public:
            cbor_decode_options() {
            }
        };

        class cbor_encode_options : public virtual cbor_options_common {
            friend class cbor_options;

            bool use_stringref_;
            bool use_typed_arrays_;
        public:
            cbor_encode_options()
                    : use_stringref_(false),
                      use_typed_arrays_(false) {
            }

            bool pack_strings() const {
                return use_stringref_;
            }

            bool use_typed_arrays() const {
                return use_typed_arrays_;
            }
        };

        class cbor_options final : public cbor_decode_options, public cbor_encode_options {
        public:
            using cbor_options_common::max_nesting_depth;
            using cbor_encode_options::pack_strings;
            using cbor_encode_options::use_typed_arrays;

            cbor_options &max_nesting_depth(int value) {
                this->max_nesting_depth_ = value;
                return *this;
            }

            cbor_options &pack_strings(bool value) {
                this->use_stringref_ = value;
                return *this;
            }

            cbor_options &use_typed_arrays(bool value) {
                this->use_typed_arrays_ = value;
                return *this;
            }
        };

    }
}
#endif  // TURBO_JSONCONS_CBOR_CBOR_OPTIONS_H_

