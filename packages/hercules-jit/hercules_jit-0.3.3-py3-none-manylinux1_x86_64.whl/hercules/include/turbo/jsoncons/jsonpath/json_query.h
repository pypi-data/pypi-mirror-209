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

#ifndef JSONCONS_JSONPATH_JSON_QUERY_HPP
#define JSONCONS_JSONPATH_JSON_QUERY_HPP

#include "turbo/jsoncons/json.h"
#include "turbo/jsoncons/jsonpath/jsonpath_expression.h"

namespace turbo {
namespace jsonpath {
     
    template<class Json>
    Json json_query(const Json& instance,
                    const typename Json::string_view_type& path, 
                    result_options options = result_options(),
                    const custom_functions<Json>& functions = custom_functions<Json>())
    {
        auto expr = make_expression<Json>(path, functions);
        return expr.evaluate(instance, options);
    }

    template<class Json,class Callback>
    typename std::enable_if<traits_extension::is_binary_function_object<Callback,const typename Json::string_type&,const Json&>::value,void>::type
    json_query(const Json& instance, 
               const typename Json::string_view_type& path, 
               Callback callback,
               result_options options = result_options(),
               const custom_functions<Json>& functions = custom_functions<Json>())
    {
        auto expr = make_expression<Json>(path, functions);
        expr.evaluate(instance, callback, options);
    }

    template<class Json, class Alloc>
    Json json_query(std::allocator_arg_t, const Alloc& alloc, 
        const Json& instance, const typename Json::string_view_type& path, 
        result_options options = result_options(),
        const custom_functions<Json>& functions = custom_functions<Json>())
    {
        auto expr = make_expression<Json>(std::allocator_arg, alloc, path, functions);
        return expr.evaluate(instance, options);
    }

    template<class Json,class Callback,class Alloc>
    typename std::enable_if<traits_extension::is_binary_function_object<Callback,const typename Json::string_type&,const Json&>::value,void>::type
    json_query(std::allocator_arg_t, const Alloc& alloc, 
        const Json& instance, const typename Json::string_view_type& path, 
        Callback callback,
        result_options options = result_options(),
        const custom_functions<Json>& functions = custom_functions<Json>())
    {
        auto expr = make_expression<Json>(std::allocator_arg, alloc, path, functions);
        expr.evaluate(instance, callback, options);
    }

    template<class Json, class T>
    typename std::enable_if<is_json_type_traits_specialized<Json,T>::value,void>::type
        json_replace(Json& instance, const typename Json::string_view_type& path, T&& new_value,
                     result_options options = result_options::nodups,
                     const custom_functions<Json>& funcs = custom_functions<Json>())
    {
        using jsonpath_traits_type = turbo::jsonpath::detail::jsonpath_traits<Json, Json&>;

        using value_type = typename jsonpath_traits_type::value_type;
        using reference = typename jsonpath_traits_type::reference;
        using evaluator_type = typename jsonpath_traits_type::evaluator_type;
        using path_expression_type = typename jsonpath_traits_type::path_expression_type;
        using json_location_type = typename jsonpath_traits_type::json_location_type;

        auto static_resources = std::make_unique<turbo::jsonpath::detail::static_resources<value_type,reference>>(funcs);
        evaluator_type evaluator;
        path_expression_type expr = evaluator.compile(*static_resources, path);

        turbo::jsonpath::detail::dynamic_resources<Json,reference> resources;
        auto callback = [&new_value](const json_location_type&, reference v)
        {
            v = std::forward<T>(new_value);
        };
        expr.evaluate(resources, instance, resources.root_path_node(), instance, callback, options);
    }

    template<class Json, class T, class Alloc>
    typename std::enable_if<is_json_type_traits_specialized<Json,T>::value,void>::type
        json_replace(std::allocator_arg_t, const Alloc& alloc, 
            Json& instance, const typename Json::string_view_type& path, T&& new_value,
            result_options options = result_options::nodups,
            const custom_functions<Json>& funcs = custom_functions<Json>())
    {
        using jsonpath_traits_type = turbo::jsonpath::detail::jsonpath_traits<Json, Json&>;

        using value_type = typename jsonpath_traits_type::value_type;
        using reference = typename jsonpath_traits_type::reference;
        using evaluator_type = typename jsonpath_traits_type::evaluator_type;
        using path_expression_type = typename jsonpath_traits_type::path_expression_type;
        using json_location_type = typename jsonpath_traits_type::json_location_type;

        auto static_resources = std::make_unique<turbo::jsonpath::detail::static_resources<value_type,reference>>(funcs, alloc);
        evaluator_type evaluator{alloc};
        path_expression_type expr = evaluator.compile(*static_resources, path);

        turbo::jsonpath::detail::dynamic_resources<Json,reference> resources{alloc};
        auto callback = [&new_value](const json_location_type&, reference v)
        {
            v = Json(std::forward<T>(new_value), semantic_tag::none);
        };
        expr.evaluate(resources, instance, resources.root_path_node(), instance, callback, options);
    }

    template<class Json, class BinaryCallback>
    typename std::enable_if<traits_extension::is_binary_function_object<BinaryCallback,const typename Json::string_type&,Json&>::value,void>::type
    json_replace(Json& instance, const typename Json::string_view_type& path , BinaryCallback callback, 
                 result_options options = result_options::nodups,
                 const custom_functions<Json>& funcs = custom_functions<Json>())
    {
        using jsonpath_traits_type = turbo::jsonpath::detail::jsonpath_traits<Json, Json&>;

        using value_type = typename jsonpath_traits_type::value_type;
        using reference = typename jsonpath_traits_type::reference;
        using evaluator_type = typename jsonpath_traits_type::evaluator_type;
        using path_expression_type = typename jsonpath_traits_type::path_expression_type;
        using json_location_type = typename jsonpath_traits_type::json_location_type;

        auto static_resources = std::make_unique<turbo::jsonpath::detail::static_resources<value_type,reference>>(funcs);
        evaluator_type evaluator;
        path_expression_type expr = evaluator.compile(*static_resources, path);

        turbo::jsonpath::detail::dynamic_resources<Json,reference> resources;

        auto f = [&callback](const json_location_type& path, reference val)
        {
            callback(path.to_string(), val);
        };
        expr.evaluate(resources, instance, resources.root_path_node(), instance, f, options);
    }

    template<class Json, class BinaryCallback, class Alloc>
    typename std::enable_if<traits_extension::is_binary_function_object<BinaryCallback,const typename Json::string_type&,Json&>::value,void>::type
    json_replace(std::allocator_arg_t, const Alloc& alloc, 
        Json& instance, const typename Json::string_view_type& path , BinaryCallback callback, 
        result_options options = result_options::nodups,
        const custom_functions<Json>& funcs = custom_functions<Json>())
    {
        using jsonpath_traits_type = turbo::jsonpath::detail::jsonpath_traits<Json, Json&>;

        using value_type = typename jsonpath_traits_type::value_type;
        using reference = typename jsonpath_traits_type::reference;
        using evaluator_type = typename jsonpath_traits_type::evaluator_type;
        using path_expression_type = typename jsonpath_traits_type::path_expression_type;
        using json_location_type = typename jsonpath_traits_type::json_location_type;

        auto static_resources = std::make_unique<turbo::jsonpath::detail::static_resources<value_type,reference>>(funcs, alloc);
        evaluator_type evaluator{alloc};
        path_expression_type expr = evaluator.compile(*static_resources, path);

        turbo::jsonpath::detail::dynamic_resources<Json,reference> resources{alloc};

        auto f = [&callback](const json_location_type& path, reference val)
        {
            callback(path.to_string(), val);
        };
        expr.evaluate(resources, instance, resources.root_path_node(), instance, f, options);
    }

    // Legacy replace function
    template<class Json, class UnaryCallback>
    typename std::enable_if<traits_extension::is_unary_function_object<UnaryCallback,Json>::value,void>::type
    json_replace(Json& instance, const typename Json::string_view_type& path , UnaryCallback callback)
    {
        using jsonpath_traits_type = turbo::jsonpath::detail::jsonpath_traits<Json, Json&>;

        using value_type = typename jsonpath_traits_type::value_type;
        using reference = typename jsonpath_traits_type::reference;
        using evaluator_type = typename jsonpath_traits_type::evaluator_type;
        using path_expression_type = typename jsonpath_traits_type::path_expression_type;
        using json_location_type = typename jsonpath_traits_type::json_location_type;

        auto static_resources = std::make_unique<turbo::jsonpath::detail::static_resources<value_type,reference>>();
        evaluator_type evaluator;
        path_expression_type expr = evaluator.compile(*static_resources, path);

        turbo::jsonpath::detail::dynamic_resources<Json,reference> resources;
        auto f = [callback](const json_location_type&, reference v)
        {
            v = callback(v);
        };
        expr.evaluate(resources, instance, resources.root_path_node(), instance, f, result_options::nodups);
    }

} // namespace jsonpath
} // namespace turbo

#endif
