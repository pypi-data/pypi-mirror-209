// Copyright 2023 Hercules author.
/*
 * Acknowledgement: This file originates from incubator-tvm
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

/*!
 * \file hercules/ir/op.h
 * \brief Common operators defined for Expr.
 *
 * \note Most of the operator defined here perform simple constant folding
 *   when the type is int32 or int64 for simplifying the index expressions.
 */
// Acknowledgement: Most operator APIs originate from Halide.
#pragma once

#include <algorithm>
#include <limits>
#include <type_traits>

#include <hercules/ir/op_expr.h>
#include <hercules/ir/prim_expr.h>
#include <hercules/ir/stmt.h>
#include <hercules/ir/type.h>

namespace hercules {
namespace ir {

// Most common operators can be overloaded by argument type(PrimExpr).
// So we put them under the root namespace.
// It is also necessary to overload operators for PrimExpr.
//
// We put more developer oriented APIs -- make_const and is_const under tir
// as they are more specific to the tir namespace.

/*!
 * \brief Get the type of the expression under the unified type system.
 *
 * This function could return a more refined type than
 * the runtime type provided by expr->dtype
 *
 * \param expr The input parameter.
 * \return The result type.
 *
 * \sa hercules/ir/type.h for discussion about the relation between Type and runtime::DataType.
 */
HERCULES_DLL Type GetType(const PrimExpr& expr);

/*!
 * \brief Get the implied DataType for storing values with type during runtime.
 *
 * \param type The input type.
 * \return The result runtime::DataType.
 *
 * \sa hercules/ir/type.h for discussion about the relation between Type and runtime::DataType.
 */
HERCULES_DLL runtime::DataType GetRuntimeDataType(const Type& type);

/*!
 * Query the maximum possible value of dtype.
 * \param dtype The data type.
 * \return the maximum possible value in this format.
 */
HERCULES_DLL PrimExpr max_value(const runtime::DataType& dtype, Span span = Span());

/*!
 * Query the minimum possible value of dtype.
 * \param dtype The data type.
 * \return the minimum possible value in this format.
 */
HERCULES_DLL PrimExpr min_value(const runtime::DataType& dtype, Span span = Span());

/*!
 * Get the value of infinity.
 * \param dtype The data type.
 * \return the infinity value in this format.
 */
HERCULES_DLL PrimExpr infinity(const runtime::DataType& dtype, Span span = Span());

/*!
 * \brief cast value to type.
 *
 * \param t the target type.
 * \param value The value
 * \return The result expression.
 * \note This function may return value if the type is the same.
 */
HERCULES_DLL PrimExpr cast(const runtime::DataType& t, PrimExpr value, Span span = Span());
/*!
 * \brief perform reinterpret cast value to type.
 *
 * \param t the target type.
 * \param value The value
 * \return The result expression.
 * \note This function may return value if the type is the same.
 */
HERCULES_DLL PrimExpr reinterpret(const runtime::DataType& t, PrimExpr value, Span span = Span());
/*!
 * \brief add operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr add(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief subtraction operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr sub(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief negation.
 *
 * \param a input.
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr neg(PrimExpr a, Span span = Span());
/*!
 * \brief multiplication operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr mul(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief division operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr div(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief left shift operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr left_shift(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief right shift operator
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr right_shift(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief greater
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr greater_than(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief greater_equal
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr greater_or_equal(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief less
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr less_than(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief less_equal
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr less_or_equal(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief equal
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr equal(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief not_equal
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr not_equal(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief and
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note This operator does eager constant folding.
 */
HERCULES_DLL PrimExpr logic_and(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief or
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note This operator does eager constant folding.
 */
HERCULES_DLL PrimExpr logic_or(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief not
 *
 * \param a left operand
 * \return The result expression.
 * \note This operator does eager constant folding.
 */
HERCULES_DLL PrimExpr logic_not(PrimExpr a, Span span = Span());
/*!
 * \brief compute trunc(a / b)
 *
 * This is the default integer division behavior in C.
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr truncdiv(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief compute the remainder of truncdiv
 *
 * This is the default integer division behavior in C.
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr truncmod(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief compute floor(a / b) where a and b are non-negative.
 *
 * Use this function for index split calculation.
 *
 * This function might take advantage of the fact
 * that a and b are non-negative.
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr indexdiv(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief compute the remainder floor(a / b) where a and b are non-negative.
 *
 * Use this function for index split calculation.
 * This function might take advantage of the fact
 * that a and b are non-negative.
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr indexmod(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief a // b
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr floordiv(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief compute the remainder of floordiv
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr floormod(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take maximum of two values
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr max(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take minimum of two values
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr min(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take bitwise and of two values
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr bitwise_and(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take bitwise or of two values
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr bitwise_or(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take bitwise xor of two values
 *
 * \param a left operand
 * \param b right operand
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr bitwise_xor(PrimExpr a, PrimExpr b, Span span = Span());
/*!
 * \brief take bitwise negation of two values
 *
 * \param a the input expression.
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr bitwise_invert(PrimExpr a, Span span = Span());
/*!
 * \brief Conditional expression.
 *
 * \param cond The condition
 * \param true_value The value when results are true.
 * \param false_value The value when results are false.
 * \return The result expression.
 * \note this function does eager constant folding for
 *       index types(int32, int64) when possible.
 */
HERCULES_DLL PrimExpr if_then_else(PrimExpr cond,
                               PrimExpr true_value,
                               PrimExpr false_value,
                               Span span = Span());
/*!
 * \brief Mark condition as likely.
 * \param cond The condition
 * \return The marked expression.
 */
HERCULES_DLL PrimExpr likely(PrimExpr cond, Span span = Span());
/*!
 * \brief Calculate power(x, y)
 * \param x The left operand.
 * \param y The right operand.
 */
HERCULES_DLL PrimExpr pow(PrimExpr x, PrimExpr y, Span span = Span());
/*!
 * \brief Calculate absolute value of x.
 * \param x The input data
 *
 * \return The aboslute value of input data x
 */
HERCULES_DLL PrimExpr abs(PrimExpr x, Span span = Span());
/*!
 * \brief Check if x is NaN.
 * \param x The input data
 * \return The result expression.
 */
HERCULES_DLL PrimExpr isnan(PrimExpr x, Span span = Span());

/*!
 * \brief Check if x is finite.
 * \param x The input data
 * \return The result expression.
 */
HERCULES_DLL PrimExpr isfinite(PrimExpr x, Span span = Span());

/*!
 * \brief Check if x is infinite.
 * \param x The input data
 * \return The result expression.
 */
HERCULES_DLL PrimExpr isinf(PrimExpr x, Span span = Span());

/*!
 * \brief Calculate floor(x)
 * \param x The input expression.
 * \return The result expression.
 */
HERCULES_DLL PrimExpr floor(PrimExpr x, Span span = Span());

/*!
 * \brief Calculate ceil(x)
 * \param x The input expression.
 * \return The result expression.
 */
HERCULES_DLL PrimExpr ceil(PrimExpr x, Span span = Span());

/*!
 * \brief Calculate round(x)
 * \param x The input expression.
 * \return The result expression.
 */
HERCULES_DLL PrimExpr round(PrimExpr x, Span span = Span());

/*!
 * \brief Calculates std::nearbyint(x)
 * \param x The input expression.
 * \return The result expression.
 * This is a faster alternate to round.
 */
HERCULES_DLL PrimExpr nearbyint(PrimExpr x, Span span = Span());

/*!
 * \brief Calculate trunc(x)
 * \param x The input expression.
 * \return The result expression.
 */
HERCULES_DLL PrimExpr trunc(PrimExpr x, Span span = Span());

/*!
 * \brief Construct a large uint constant by its low 32 bits and high 32bits.
 * \param dtype The final data type.
 * \param low The lower 32 bits.
 * \param high The higher 32 bits.
 * \return The constructed expression.
 */
HERCULES_DLL PrimExpr LargeUIntImm(runtime::DataType dtype,
                               int64_t low,
                               int64_t high,
                               Span span = Span());

/*!
 * \brief Execute a multiplication between two Q-numbers x and y
 * followed by a right shift s. The mathematical expression is:
 *
 *    out = round(x*y*2^-s)
 *
 * Please note that the two Q-numbers x and y are supposed to have
 * the same number of fractional bits q.
 *
 * More about Q-numbers here: https://en.wikipedia.org/wiki/Q_(number_format)
 *
 * The rounding rule is to the nearest value, rounding half up
 * (i.e., round(x.1) = x and round (x.5) = x+1)
 * \param x first Q-number
 * \param y second Q-number
 * \param q number of fractional bits in x and y. Needs to be > 0
 * \param s integer right shift
 * \return The constructed expression.
 */
HERCULES_DLL PrimExpr
q_multiply_shift(PrimExpr x, PrimExpr y, PrimExpr q, PrimExpr s, Span span = Span());

// Intrinsic operators
#define HERCULES_DECLARE_INTRIN_UNARY(OpName)                  \
  inline PrimExpr OpName(PrimExpr x, Span span) {                \
    static const Op& op = Op::Get("ir." #OpName);                \
    return ::hercules::ir::PrimCall(x.dtype(), op, {x}, span); \
  }

HERCULES_DECLARE_INTRIN_UNARY(pow);
HERCULES_DECLARE_INTRIN_UNARY(exp);
HERCULES_DECLARE_INTRIN_UNARY(exp2);
HERCULES_DECLARE_INTRIN_UNARY(exp10);
HERCULES_DECLARE_INTRIN_UNARY(erf);
HERCULES_DECLARE_INTRIN_UNARY(tanh);
HERCULES_DECLARE_INTRIN_UNARY(sigmoid);
HERCULES_DECLARE_INTRIN_UNARY(sqrt);
HERCULES_DECLARE_INTRIN_UNARY(rsqrt);
HERCULES_DECLARE_INTRIN_UNARY(log);
HERCULES_DECLARE_INTRIN_UNARY(log2);
HERCULES_DECLARE_INTRIN_UNARY(log10);
HERCULES_DECLARE_INTRIN_UNARY(popcount);
HERCULES_DECLARE_INTRIN_UNARY(tan);
HERCULES_DECLARE_INTRIN_UNARY(cos);
HERCULES_DECLARE_INTRIN_UNARY(cosh);
HERCULES_DECLARE_INTRIN_UNARY(sin);
HERCULES_DECLARE_INTRIN_UNARY(sinh);
HERCULES_DECLARE_INTRIN_UNARY(asin);
HERCULES_DECLARE_INTRIN_UNARY(acos);
HERCULES_DECLARE_INTRIN_UNARY(atan);
HERCULES_DECLARE_INTRIN_UNARY(acosh);
HERCULES_DECLARE_INTRIN_UNARY(asinh);
HERCULES_DECLARE_INTRIN_UNARY(atanh);

#define HERCULES_DECLARE_INTRIN_BINARY(OpName)                    \
  inline PrimExpr OpName(PrimExpr x, PrimExpr y, Span span) {       \
    static const Op& op = Op::Get("ir." #OpName);                   \
    return ::hercules::ir::PrimCall(x.dtype(), op, {x, y}, span); \
  }

HERCULES_DECLARE_INTRIN_BINARY(atan2);
HERCULES_DECLARE_INTRIN_BINARY(nextafter);
HERCULES_DECLARE_INTRIN_BINARY(copysign);
HERCULES_DECLARE_INTRIN_BINARY(hypot);
HERCULES_DECLARE_INTRIN_BINARY(ldexp);

/*!
 * \brief Check if type is a pointer to a runtime element type.
 * \param type The type to be checked.
 * \param element_type The corresponding element type.
 * \return The check results
 */
inline bool IsPointerType(const Type& type, const runtime::DataType& element_type) {
  if (!type.defined())
    return false;
  if (const auto* ptr_type = type.as<PointerTypeNode>()) {
    if (const auto* prim_type = ptr_type->element_type.as<PrimTypeNode>()) {
      return prim_type->dtype == element_type;
    }
  }
  return false;
}

/*!
 * \brief Make a const value with certain data type.
 * \param t The target type.
 * \param value The input value
 * \return the result expression.
 * \tparam ValueType The constant value type
 */
template <typename ValueType,
          typename = typename std::enable_if<std::is_pod<ValueType>::value>::type>
inline PrimExpr make_const(runtime::DataType t, ValueType value, Span span = Span());
/*!
 * \brief Make a const zero expr.
 * \param t The target type.
 * \return the result expression.
 */
inline PrimExpr make_zero(runtime::DataType t, Span span = Span());
/*!
 * \brief Make a constant true expression.
 * \param lanes The number of lanes in the bool
 * \return The result expression.
 */
inline PrimExpr const_true(int lanes = 1, Span span = Span()) {
  return make_const(runtime::DataType::UInt(1, lanes), 1, span);
}
/*!
 * \brief Make a constant false expression.
 * \param lanes The number of lanes in the bool
 * \return The result expression.
 */
inline PrimExpr const_false(int lanes = 1, Span span = Span()) {
  return make_const(runtime::DataType::UInt(1, lanes), 0, span);
}
/*!
 * \brief Get x as constant int expression.
 * \param x The expression
 * \return the address to the int expression,
 *         return nullptr, if x is not IntImm.
 */
inline const int64_t* as_const_int(const PrimExpr& x) {
  if (!x.defined())
    return nullptr;
  if (const IntImmNode* op = x.as<IntImmNode>()) {
    return &(op->value);
  } else {
    return nullptr;
  }
}

/*!
 * \brief Check whether x is a constant integer expression.
 * \param x The input argument
 * \param value the value to be compared against.
 * \return whether x is constant expression.
 */
inline bool is_const_int(const PrimExpr& x, int64_t value);

/*!
 * \brief Check whether stmt is nop.
 * \param stmt The input statement
 * \return whether stmt is nop
 */
inline bool is_no_op(const Stmt& stmt);

/*!
 * \brief Check whether x is a constant integer 1
 * \param x The input argument.
 * \note This only return true for integer types.
 * \return whether x is constant 1
 */
inline bool is_one(const PrimExpr& x) {
  return is_const_int(x, 1);
}

/*!
 * \brief Check whether x is a constant integer 0
 * \param x The input argument
 * \return whether x is constant 0
 * \note This only return true for integer types.
 */
inline bool is_zero(const PrimExpr& x) {
  return is_const_int(x, 0);
}

/*!
 * \brief Check whether x is an integer constant.
 * \note This only return true for integer types.
 * \return whether x is constant
 */
inline bool is_const_int(const PrimExpr& x);

/*!
 * \brief Check whether x is an integer/float constant.
 * \note This only return true for integer types.
 * \return whether x is constant
 */
inline bool is_const_number(const PrimExpr& x);

/*!
 * \brief Left fold.
 * \param freduce The reduction function.
 * \param init_value The initial value.
 * \param values The values to be folded.
 * \param span The location of the fold in the source.
 * \return The result.
 * \tparam FReduce The type of the reduction.
 */
template <typename FReduce>
inline PrimExpr foldl(FReduce freduce,
                      PrimExpr init_value,
                      const Array<PrimExpr>& values,
                      Span span = Span());

/*!
 * \brief Check whether x is a constant power of two
 * If x is power of two, write the power to the shift.
 *
 * \param x The input expression.
 * \param shift The output shift if x is power of two.
 * \return whether x is constant power of two
 */
HERCULES_DLL bool is_const_power_of_two_integer(const PrimExpr& x, int* shift);

// Implementation details after this
inline bool is_const_int(const PrimExpr& x) {
  if (x.as<IntImmNode>()) {
    return true;
  }
  return false;
}

inline bool is_const_number(const PrimExpr& x) {
  if (x.as<IntImmNode>()) {
    return true;
  } else if (x.as<FloatImmNode>()) {
    return true;
  }
  return false;
}

inline bool is_positive_const(const PrimExpr& a) {
  if (const IntImmNode* op = a.as<IntImmNode>()) {
    return op->value > 0;
  } else {
    return false;
  }
}

inline bool is_negative_const(const PrimExpr& a) {
  if (const IntImmNode* op = a.as<IntImmNode>()) {
    return op->value < 0;
  } else {
    return false;
  }
}

inline bool is_const_int(const PrimExpr& x, int64_t value) {
  if (const auto* op = x.as<IntImmNode>()) {
    return op->value == value;
  }
  return false;
}

inline bool is_no_op(const Stmt& stmt) {
  if (!stmt.defined())
    return true;
  if (const auto* op = stmt.as<ExprStmtNode>()) {
    if (op->expr.as<PrimExprNode>()) {
      return is_const_int(runtime::Downcast<PrimExpr>(op->expr));
    }
  }
  if (const auto* op = stmt.as<SeqStmtNode>()) {
    return op->seq.size() == 0;
  }
  return false;
}

template <typename ValueType>
inline PrimExpr MakeConstScalar(runtime::DataType t, ValueType value, Span span = Span()) {
  if (t.is_int())
    return IntImm(t, static_cast<int64_t>(value), span);
  if (t.is_uint()) {
    // Use IntImm if it is a small integer
    uint64_t uval = static_cast<uint64_t>(value);
    if (value < static_cast<ValueType>(0)) {
      MXLOG(FATAL) << "cannot make uint from negative value " << value;
    } else if (uval <= static_cast<uint64_t>(std::numeric_limits<int64_t>::max())) {
      return IntImm(t, static_cast<int64_t>(value), span);
    } else {
      uint64_t mask = (static_cast<uint64_t>(1) << 32U) - 1U;
      uint64_t low = uval & mask;
      uint64_t high = uval >> 32U;
      return LargeUIntImm(t, static_cast<int64_t>(low), static_cast<int64_t>(high), span);
    }
  }
  if (t.is_float() || t.is_bfloat16())
    return FloatImm(t, static_cast<double>(value), span);
  // For now, we store const scalar values of custom datatypes within doubles; later, during the
  // datatypes lowering pass, we will lower the value to its true representation in the format
  // specified by the datatype.
  // TODO(gus) when do we need to start worrying about doubles not being precise enough?
  if (static_cast<uint8_t>(t.code()) >= static_cast<uint8_t>(runtime::DataType::kCustomBegin)) {
    return FloatImm(t, static_cast<double>(value), span);
  }
  MXLOG(FATAL) << "cannot make const for type " << t;
  return PrimExpr();
}

template <typename ValueType, typename>
inline PrimExpr make_const(runtime::DataType t, ValueType value, Span span) {
  MXCHECK(t.lanes() == 1);
  return MakeConstScalar(t, value, span);
}

inline PrimExpr make_zero(runtime::DataType t, Span span) {
  if (t.is_handle()) {
    return reinterpret(t, make_const(runtime::DataType::UInt(64), 0, span), span);
  }
  return make_const(t, 0, span);
}

template <typename FReduce>
inline PrimExpr foldl(FReduce freduce,
                      PrimExpr init_value,
                      const Array<PrimExpr>& values,
                      Span span) {
  for (PrimExpr val : values) {
    init_value = freduce(init_value, val, span);
  }
  return init_value;
}

// additional const expression overloading
#define HERCULES_DEFINE_ASSIGN_OP_OVERLOAD(Name, OpFunc)            \
  inline PrimExpr Name(PrimExpr& a, PrimExpr b, Span span = Span()) { \
    a = OpFunc(a, b, span);                                           \
    return a;                                                         \
  }

#define HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(Name)                                 \
  inline PrimExpr Name(const PrimExpr& a, float b, Span span = Span()) {                 \
    return Name(a, PrimExpr(b), span);                                                   \
  }                                                                                      \
  inline PrimExpr Name(float a, const PrimExpr& b, Span span = Span()) {                 \
    return Name(PrimExpr(a), b, span);                                                   \
  }                                                                                      \
  inline PrimExpr Name(int a, const PrimExpr& b, Span span = Span()) {                   \
    return Name(::hercules::ir::make_const(b.dtype(), a), b, span);                    \
  }                                                                                      \
  inline PrimExpr Name(const PrimExpr& a, int b, Span span = Span()) {                   \
    return Name(a, ::hercules::ir::make_const(a.dtype(), b), span);                    \
  }                                                                                      \
  inline PrimExpr Name(const PrimExpr& a, double b, Span span = Span()) {                \
    return Name(a, ::hercules::ir::make_const(runtime::DataType::Float(64), b), span); \
  }

#define HERCULES_DEFINE_LOGICAL_OP_CONST_VAL_OVERLOAD(Name)           \
  inline PrimExpr Name(const PrimExpr& a, bool b, Span span = Span()) { \
    return Name(a, PrimExpr(b), span);                                  \
  }                                                                     \
  inline PrimExpr Name(bool a, const PrimExpr& b, Span span = Span()) { \
    return Name(PrimExpr(a), b, span);                                  \
  }

#define HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(Name)              \
  inline PrimExpr Name(const PrimExpr& a, int b, Span span = Span()) { \
    return Name(a, ::hercules::ir::make_const(a.dtype(), b), span);  \
  }                                                                    \
  inline PrimExpr Name(int a, const PrimExpr& b, Span span = Span()) { \
    return Name(::hercules::ir::make_const(b.dtype(), a), b, span);  \
  }

HERCULES_DEFINE_ASSIGN_OP_OVERLOAD(add_assign, add);
HERCULES_DEFINE_ASSIGN_OP_OVERLOAD(sub_assign, sub);
HERCULES_DEFINE_ASSIGN_OP_OVERLOAD(mul_assign, mul);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(add);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(sub);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(mul);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(max);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(min);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(div);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(greater_than);  // NOLINT(*)
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(greater_or_equal);
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(less_than);  // NOLINT(*)
HERCULES_DEFINE_BINOP_CONST_VAL_OVERLOAD(less_or_equal);
// integer related ops
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(indexdiv);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(indexmod);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(truncdiv);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(truncmod);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(floordiv);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(floormod);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(right_shift);  // NOLINT(*)
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(left_shift);   // NOLINT(*)
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(bitwise_and);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(bitwise_or);
HERCULES_DEFINE_INT_OP_CONST_VAL_OVERLOAD(bitwise_xor);
// logical ops
HERCULES_DEFINE_LOGICAL_OP_CONST_VAL_OVERLOAD(logic_and);
HERCULES_DEFINE_LOGICAL_OP_CONST_VAL_OVERLOAD(logic_or);

/*!
 * \brief Helper function to raise a compiler error about division ambiguity.
 * \note The call to this function will always results in a compiler error.
 * \tparam TA Any class type.
 */
template <typename TA>
inline void DivAmbiguityError(const TA& a) {
  constexpr bool div_ambiguity = !std::is_class<TA>::value;
  static_assert(div_ambiguity,
                "Hercules supports multiple types of integer divisions, "
                "please call div, indexdiv/indexmod, "
                "floordiv/floormod or truncdiv/truncmod directly "
                "to avoid ambiguity in the code. "
                "Checkout these functions in expr_operator.h.");
}

// The following code are not intended to be used in the codebase.
// Instead, they generate clear compiler errors that ask developers
// to use the specific division function.
// The second template argument is necessary to make sure the
// code compiles lazily by the compiler during invocation.
template <typename TB>
inline PrimExpr operator/(const PrimExpr& a, const TB& b) {
  DivAmbiguityError(a);
  return a;
}

template <typename TB>
inline PrimExpr operator/=(const PrimExpr& a, const TB& b) {
  DivAmbiguityError(a);
  return a;
}

template <typename TB>
inline PrimExpr operator%(const PrimExpr& a, const TB& b) {
  DivAmbiguityError(a);
  return a;
}

}  // namespace ir
}  // namespace hercules
