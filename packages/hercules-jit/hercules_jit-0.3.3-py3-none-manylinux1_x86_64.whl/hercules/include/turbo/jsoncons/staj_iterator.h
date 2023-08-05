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

#ifndef TURBO_JSONCONS_STAJ_ITERATOR_H_
#define TURBO_JSONCONS_STAJ_ITERATOR_H_

#include <new> // placement new
#include <memory>
#include <string>
#include <stdexcept>
#include <system_error>
#include <ios>
#include <iterator> // std::input_iterator_tag
#include "turbo/jsoncons/json_exception.h"
#include "turbo/jsoncons/staj_cursor.h"
#include "turbo/jsoncons/basic_json.h"
#include "turbo/jsoncons/decode_traits.h"

namespace turbo {

    template<class T, class Json>
    class staj_array_view;

    template<class T, class Json>
    class staj_array_iterator {
        using char_type = typename Json::char_type;

        staj_array_view<T, Json> *view_;
        std::exception_ptr eptr_;

    public:
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T *;
        using reference = T &;
        using iterator_category = std::input_iterator_tag;

        staj_array_iterator() noexcept
                : view_(nullptr) {
        }

        staj_array_iterator(staj_array_view<T, Json> &view)
                : view_(std::addressof(view)) {
            if (view_->cursor_->current().event_type() == staj_event_type::begin_array) {
                next();
            } else {
                view_->cursor_ = nullptr;
            }
        }

        staj_array_iterator(staj_array_view<T, Json> &view,
                            std::error_code &ec)
                : view_(std::addressof(view)) {
            if (view_->cursor_->current().event_type() == staj_event_type::begin_array) {
                next(ec);
                if (ec) { view_ = nullptr; }
            } else {
                view_ = nullptr;
            }
        }

        ~staj_array_iterator() noexcept {
        }

        bool has_value() const {
            return !eptr_;
        }

        const T &operator*() const {
            if (eptr_) {
                std::rethrow_exception(eptr_);
            } else {
                return *view_->value_;
            }
        }

        const T *operator->() const {
            if (eptr_) {
                std::rethrow_exception(eptr_);
            } else {
                return view_->value_.operator->();
            }
        }

        staj_array_iterator &operator++() {
            next();
            return *this;
        }

        staj_array_iterator &increment(std::error_code &ec) {
            next(ec);
            if (ec) { view_ = nullptr; }
            return *this;
        }

        staj_array_iterator operator++(int) // postfix increment
        {
            staj_array_iterator temp(*this);
            next();
            return temp;
        }

        friend bool operator==(const staj_array_iterator &a, const staj_array_iterator &b) {
            return (!a.view_ && !b.view_)
                   || (!a.view_ && b.done())
                   || (!b.view_ && a.done());
        }

        friend bool operator!=(const staj_array_iterator &a, const staj_array_iterator &b) {
            return !(a == b);
        }

    private:

        bool done() const {
            return view_->cursor_->done() || view_->cursor_->current().event_type() == staj_event_type::end_array;
        }

        void next() {
            std::error_code ec;
            next(ec);
            if (ec) {
                JSONCONS_THROW(ser_error(ec, view_->cursor_->context().line(), view_->cursor_->context().column()));
            }
        }

        void next(std::error_code &ec) {
            using char_type = typename Json::char_type;

            if (!done()) {
                view_->cursor_->next(ec);
                if (ec) {
                    return;
                }
                if (!done()) {
                    eptr_ = std::exception_ptr();
                    JSONCONS_TRY {
                        view_->value_ = decode_traits<T, char_type>::decode(*view_->cursor_, view_->decoder_, ec);
                    }
                    JSONCONS_CATCH(const conv_error&) {
                        eptr_ = std::current_exception();
                    }
                }
            }
        }
    };

    template<class Key, class Json, class T=Json>
    class staj_object_view;

    template<class Key, class T, class Json>
    class staj_object_iterator {
        using char_type = typename Json::char_type;

        staj_object_view<Key, T, Json> *view_;
        std::exception_ptr eptr_;
    public:
        using key_type = std::basic_string<char_type>;
        using value_type = std::pair<key_type, T>;
        using difference_type = std::ptrdiff_t;
        using pointer = value_type *;
        using reference = value_type &;
        using iterator_category = std::input_iterator_tag;

    public:

        staj_object_iterator() noexcept
                : view_(nullptr) {
        }

        staj_object_iterator(staj_object_view<Key, T, Json> &view)
                : view_(std::addressof(view)) {
            if (view_->cursor_->current().event_type() == staj_event_type::begin_object) {
                next();
            } else {
                view_ = nullptr;
            }
        }

        staj_object_iterator(staj_object_view<Key, T, Json> &view,
                             std::error_code &ec)
                : view_(std::addressof(view)) {
            if (view_->cursor_->current().event_type() == staj_event_type::begin_object) {
                next(ec);
                if (ec) { view_ = nullptr; }
            } else {
                view_ = nullptr;
            }
        }

        ~staj_object_iterator() noexcept {
        }

        bool has_value() const {
            return !eptr_;
        }

        const value_type &operator*() const {
            if (eptr_) {
                std::rethrow_exception(eptr_);
            } else {
                return *view_->key_value_;
            }
        }

        const value_type *operator->() const {
            if (eptr_) {
                std::rethrow_exception(eptr_);
            } else {
                return view_->key_value_.operator->();
            }
        }

        staj_object_iterator &operator++() {
            next();
            return *this;
        }

        staj_object_iterator &increment(std::error_code &ec) {
            next(ec);
            if (ec) {
                view_ = nullptr;
            }
            return *this;
        }

        staj_object_iterator operator++(int) // postfix increment
        {
            staj_object_iterator temp(*this);
            next();
            return temp;
        }

        friend bool operator==(const staj_object_iterator &a, const staj_object_iterator &b) {
            return (!a.view_ && !b.view_)
                   || (!a.view_ && b.done())
                   || (!b.view_ && a.done());
        }

        friend bool operator!=(const staj_object_iterator &a, const staj_object_iterator &b) {
            return !(a == b);
        }

    private:

        bool done() const {
            return view_->cursor_->done() || view_->cursor_->current().event_type() == staj_event_type::end_object;
        }

        void next() {
            std::error_code ec;
            next(ec);
            if (ec) {
                JSONCONS_THROW(ser_error(ec, view_->cursor_->context().line(), view_->cursor_->context().column()));
            }
        }

        void next(std::error_code &ec) {
            using char_type = typename Json::char_type;

            view_->cursor_->next(ec);
            if (ec) {
                return;
            }
            if (!done()) {
                TURBO_ASSERT(view_->cursor_->current().event_type() == staj_event_type::key);
                auto key = view_->cursor_->current().template get<key_type>();
                view_->cursor_->next(ec);
                if (ec) {
                    return;
                }
                if (!done()) {
                    eptr_ = std::exception_ptr();
                    JSONCONS_TRY {
                        view_->key_value_ = value_type(std::move(key),
                                                       decode_traits<T, char_type>::decode(*view_->cursor_,
                                                                                           view_->decoder_, ec));
                    }
                    JSONCONS_CATCH(const conv_error&) {
                        eptr_ = std::current_exception();
                    }
                }
            }
        }
    };

    // staj_array_view

    template<class T, class Json>
    class staj_array_view {
        friend class staj_array_iterator<T, Json>;

    public:
        using char_type = typename Json::char_type;
        using iterator = staj_array_iterator<T, Json>;
    private:
        basic_staj_cursor<char_type> *cursor_;
        json_decoder<Json> decoder_;
        std::optional<T> value_;
    public:
        staj_array_view(basic_staj_cursor<char_type> &cursor)
                : cursor_(std::addressof(cursor)) {
        }

        iterator begin() {
            return staj_array_iterator<T, Json>(*this);
        }

        iterator end() {
            return staj_array_iterator<T, Json>();
        }
    };

    // staj_object_view

    template<class Key, class T, class Json>
    class staj_object_view {
        friend class staj_object_iterator<Key, T, Json>;

    public:
        using char_type = typename Json::char_type;
        using iterator = staj_object_iterator<Key, T, Json>;
        using key_type = std::basic_string<char_type>;
        using value_type = std::pair<key_type, T>;
    private:
        basic_staj_cursor<char_type> *cursor_;
        json_decoder<Json> decoder_;
        std::optional<value_type> key_value_;
    public:
        staj_object_view(basic_staj_cursor<char_type> &cursor)
                : cursor_(std::addressof(cursor)) {
        }

        iterator begin() {
            return staj_object_iterator<Key, T, Json>(*this);
        }

        iterator end() {
            return staj_object_iterator<Key, T, Json>();
        }
    };

    template<class T, class CharT, class Json=typename std::conditional<traits_extension::is_basic_json<T>::value, T, basic_json<CharT>>::type>
    staj_array_view<T, Json> staj_array(basic_staj_cursor<CharT> &cursor) {
        return staj_array_view<T, Json>(cursor);
    }

    template<class Key, class T, class CharT, class Json=typename std::conditional<traits_extension::is_basic_json<T>::value, T, basic_json<CharT>>::type>
    staj_object_view<Key, T, Json> staj_object(basic_staj_cursor<CharT> &cursor) {
        return staj_object_view<Key, T, Json>(cursor);
    }

} // namespace turbo

#endif  // TURBO_JSONCONS_STAJ_ITERATOR_H_

