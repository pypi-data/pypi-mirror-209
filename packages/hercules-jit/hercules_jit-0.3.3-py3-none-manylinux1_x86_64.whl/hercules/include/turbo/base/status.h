// Copyright 2022 The Turbo Authors.
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
// -----------------------------------------------------------------------------
// File: status.h
// -----------------------------------------------------------------------------
//
// This header file defines the Turbo `status` library, consisting of:
//
//   * An `turbo::Status` class for holding error handling information
//   * A set of canonical `turbo::StatusCode` error codes, and associated
//     utilities for generating and propagating status codes.
//   * A set of helper functions for creating status codes and checking their
//     values
//
// Within Google, `turbo::Status` is the primary mechanism for communicating
// errors in C++, and is used to represent error state in both in-process
// library calls as well as RPC calls. Some of these errors may be recoverable,
// but others may not. Most functions that can produce a recoverable error
// should be designed to return an `turbo::Status` (or `turbo::ResultStatus`).
//
// Example:
//
// turbo::Status myFunction(std::string_view fname, ...) {
//   ...
//   // encounter error
//   if (error condition) {
//     return turbo::InvalidArgumentError("bad mode");
//   }
//   // else, return OK
//   return turbo::OkStatus();
// }
//
// An `turbo::Status` is designed to either return "OK" or one of a number of
// different error codes, corresponding to typical error conditions.
// In almost all cases, when using `turbo::Status` you should use the canonical
// error codes (of type `turbo::StatusCode`) enumerated in this header file.
// These canonical codes are understood across the codebase and will be
// accepted across all API and RPC boundaries.
#ifndef TURBO_BASE_STATUS_H_
#define TURBO_BASE_STATUS_H_

#include <ostream>
#include <string>
#include <utility>

#include "turbo/meta/function_ref.h"
#include "turbo/meta/optional.h"
#include "turbo/base/internal/status_internal.h"
#include "turbo/strings/cord.h"
#include "turbo/strings/string_view.h"
#include "turbo/strings/str_format.h"
#include "turbo/base/turbo_error.h"
#include "turbo/base/turbo_module.h"

namespace turbo {
TURBO_NAMESPACE_BEGIN

    // turbo::StatusCode
    //
    // An `turbo::StatusCode` is an enumerated type indicating either no error ("OK")
    // or an error condition. In most cases, an `turbo::Status` indicates a
    // recoverable error, and the purpose of signalling an error is to indicate what
    // action to take in response to that error. These error codes map to the proto
    // RPC error codes indicated in https://cloud.google.com/apis/design/errors.
    //
    // The errors listed below are the canonical errors associated with
    // `turbo::Status` and are used throughout the codebase. As a result, these
    // error codes are somewhat generic.
    //
    // In general, try to return the most specific error that applies if more than
    // one error may pertain. For example, prefer `kOutOfRange` over
    // `kFailedPrecondition` if both codes apply. Similarly prefer `kNotFound` or
    // `kAlreadyExists` over `kFailedPrecondition`.
    //
    // Because these errors may cross RPC boundaries, these codes are tied to the
    // `google.rpc.Code` definitions within
    // https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
    // The string value of these RPC codes is denoted within each enum below.
    //
    // If your error handling code requires more context, you can attach payloads
    // to your status. See `turbo::Status::SetPayload()` and
    // `turbo::Status::GetPayload()` below.
    ///  using StatusCode =  int;
  // StatusCode::kOk
  //
  // kOK (gRPC code "OK") does not indicate an error; this value is returned on
  // success. It is typical to check for this value before proceeding on any
  // given call across an API or RPC boundary. To check this value, use the
  // `turbo::Status::ok()` member function rather than inspecting the raw code.
  static constexpr StatusCode kOk = 0;

  // StatusCode::kCancelled
  //
  // kCancelled (gRPC code "CANCELLED") indicates the operation was cancelled,
  // typically by the caller.
  static constexpr StatusCode kCancelled = 1;

  // StatusCode::kUnknown
  //
  // kUnknown (gRPC code "UNKNOWN") indicates an unknown error occurred. In
  // general, more specific errors should be raised, if possible. Errors raised
  // by APIs that do not return enough error information may be converted to
  // this error.
  static constexpr StatusCode kUnknown = 2;

  // StatusCode::kInvalidArgument
  //
  // kInvalidArgument (gRPC code "INVALID_ARGUMENT") indicates the caller
  // specified an invalid argument, such as a malformed filename. Note that use
  // of such errors should be narrowly limited to indicate the invalid nature of
  // the arguments themselves. Errors with validly formed arguments that may
  // cause errors with the state of the receiving system should be denoted with
  // `kFailedPrecondition` instead.
  static constexpr StatusCode kInvalidArgument = 3;

  // StatusCode::kDeadlineExceeded
  //
  // kDeadlineExceeded (gRPC code "DEADLINE_EXCEEDED") indicates a deadline
  // expired before the operation could complete. For operations that may change
  // state within a system, this error may be returned even if the operation has
  // completed successfully. For example, a successful response from a server
  // could have been delayed long enough for the deadline to expire.
  static constexpr StatusCode kDeadlineExceeded = 4;

  // StatusCode::kNotFound
  //
  // kNotFound (gRPC code "NOT_FOUND") indicates some requested entity (such as
  // a file or directory) was not found.
  //
  // `kNotFound` is useful if a request should be denied for an entire class of
  // users, such as during a gradual feature rollout or undocumented allow list.
  // If a request should be denied for specific sets of users, such as through
  // user-based access control, use `kPermissionDenied` instead.
  static constexpr StatusCode kNotFound = 5;

  // StatusCode::kAlreadyExists
  //
  // kAlreadyExists (gRPC code "ALREADY_EXISTS") indicates that the entity a
  // caller attempted to create (such as a file or directory) is already
  // present.
  static constexpr StatusCode kAlreadyExists = 6;

  // StatusCode::kPermissionDenied
  //
  // kPermissionDenied (gRPC code "PERMISSION_DENIED") indicates that the caller
  // does not have permission to execute the specified operation. Note that this
  // error is different than an error due to an *un*authenticated user. This
  // error code does not imply the request is valid or the requested entity
  // exists or satisfies any other pre-conditions.
  //
  // `kPermissionDenied` must not be used for rejections caused by exhausting
  // some resource. Instead, use `kResourceExhausted` for those errors.
  // `kPermissionDenied` must not be used if the caller cannot be identified.
  // Instead, use `kUnauthenticated` for those errors.
  static constexpr StatusCode kPermissionDenied = 7;

  // StatusCode::kResourceExhausted
  //
  // kResourceExhausted (gRPC code "RESOURCE_EXHAUSTED") indicates some resource
  // has been exhausted, perhaps a per-user quota, or perhaps the entire file
  // system is out of space.
  static constexpr StatusCode kResourceExhausted = 8;

  // StatusCode::kFailedPrecondition
  //
  // kFailedPrecondition (gRPC code "FAILED_PRECONDITION") indicates that the
  // operation was rejected because the system is not in a state required for
  // the operation's execution. For example, a directory to be deleted may be
  // non-empty, an "rmdir" operation is applied to a non-directory, etc.
  //
  // Some guidelines that may help a service implementer in deciding between
  // `kFailedPrecondition`, `kAborted`, and `kUnavailable`:
  //
  //  (a) Use `kUnavailable` if the client can retry just the failing call.
  //  (b) Use `kAborted` if the client should retry at a higher transaction
  //      level (such as when a client-specified test-and-set fails, indicating
  //      the client should restart a read-modify-write sequence).
  //  (c) Use `kFailedPrecondition` if the client should not retry until
  //      the system state has been explicitly fixed. For example, if a "rmdir"
  //      fails because the directory is non-empty, `kFailedPrecondition`
  //      should be returned since the client should not retry unless
  //      the files are deleted from the directory.
  static constexpr StatusCode kFailedPrecondition = 9;

  // StatusCode::kAborted
  //
  // kAborted (gRPC code "ABORTED") indicates the operation was aborted,
  // typically due to a concurrency issue such as a sequencer check failure or a
  // failed transaction.
  //
  // See the guidelines above for deciding between `kFailedPrecondition`,
  // `kAborted`, and `kUnavailable`.
  static constexpr StatusCode kAborted = 10;

  // StatusCode::kOutOfRange
  //
  // kOutOfRange (gRPC code "OUT_OF_RANGE") indicates the operation was
  // attempted past the valid range, such as seeking or reading past an
  // end-of-file.
  //
  // Unlike `kInvalidArgument`, this error indicates a problem that may
  // be fixed if the system state changes. For example, a 32-bit file
  // system will generate `kInvalidArgument` if asked to read at an
  // offset that is not in the range [0,2^32-1], but it will generate
  // `kOutOfRange` if asked to read from an offset past the current
  // file size.
  //
  // There is a fair bit of overlap between `kFailedPrecondition` and
  // `kOutOfRange`.  We recommend using `kOutOfRange` (the more specific
  // error) when it applies so that callers who are iterating through
  // a space can easily look for an `kOutOfRange` error to detect when
  // they are done.
  static constexpr StatusCode kOutOfRange = 11;

  // StatusCode::kUnimplemented
  //
  // kUnimplemented (gRPC code "UNIMPLEMENTED") indicates the operation is not
  // implemented or supported in this service. In this case, the operation
  // should not be re-attempted.
  static constexpr StatusCode kUnimplemented = 12;

  // StatusCode::kInternal
  //
  // kInternal (gRPC code "INTERNAL") indicates an internal error has occurred
  // and some invariants expected by the underlying system have not been
  // satisfied. This error code is reserved for serious errors.
  static constexpr StatusCode kInternal = 13;

  // StatusCode::kUnavailable
  //
  // kUnavailable (gRPC code "UNAVAILABLE") indicates the service is currently
  // unavailable and that this is most likely a transient condition. An error
  // such as this can be corrected by retrying with a backoff scheme. Note that
  // it is not always safe to retry non-idempotent operations.
  //
  // See the guidelines above for deciding between `kFailedPrecondition`,
  // `kAborted`, and `kUnavailable`.
  static constexpr StatusCode kUnavailable = 14;

  // StatusCode::kDataLoss
  //
  // kDataLoss (gRPC code "DATA_LOSS") indicates that unrecoverable data loss or
  // corruption has occurred. As this error is serious, proper alerting should
  // be attached to errors such as this.
  static constexpr StatusCode kDataLoss = 15;

  // StatusCode::kUnauthenticated
  //
  // kUnauthenticated (gRPC code "UNAUTHENTICATED") indicates that the request
  // does not have valid authentication credentials for the operation. Correct
  // the authentication and try again.
  static constexpr StatusCode kUnauthenticated = 16;

  // StatusCode::DoNotUseReservedForFutureExpansionUseDefaultInSwitchInstead_
  //
  // NOTE: this error code entry should not be used and you should not rely on
  // its value, which may change.
  //
  // The purpose of this enumerated value is to force people who handle status
  // codes with `switch()` statements to *not* simply enumerate all possible
  // values, but instead provide a "default:" case. Providing such a default
  // case ensures that code will compile when new codes are added.
  static constexpr StatusCode kDoNotUseReservedForFutureExpansionUseDefaultInSwitchInstead_ = 20;

// StatusCodeToString()
//
// Returns the name for the status code, or "" if it is an unknown value.
std::string StatusCodeToString(StatusCode code);

// operator<<
//
// Streams StatusCodeToString(code) to `os`.
std::ostream& operator<<(std::ostream& os, StatusCode code);

// turbo::StatusToStringMode
//
// An `turbo::StatusToStringMode` is an enumerated type indicating how
// `turbo::Status::ToString()` should construct the output string for a non-ok
// status.
enum class StatusToStringMode : int {
  // ToString will not contain any extra data (such as payloads). It will only
  // contain the error code and message, if any.
  kWithNoExtraData = 0,
  // ToString will contain the payloads.
  kWithPayload = 1 << 0,
  // ToString will contain the module name.
  kWithModule = 1 << 1,
  // ToString will include all the extra data this Status has.
  kWithEverything = ~kWithNoExtraData,
  // Default mode used by ToString. Its exact value might change in the future.
  kDefault = kWithPayload,
};

// turbo::StatusToStringMode is specified as a bitmask type, which means the
// following operations must be provided:
inline constexpr StatusToStringMode operator&(StatusToStringMode lhs,
                                              StatusToStringMode rhs) {
  return static_cast<StatusToStringMode>(static_cast<int>(lhs) &
                                         static_cast<int>(rhs));
}
inline constexpr StatusToStringMode operator|(StatusToStringMode lhs,
                                              StatusToStringMode rhs) {
  return static_cast<StatusToStringMode>(static_cast<int>(lhs) |
                                         static_cast<int>(rhs));
}
inline constexpr StatusToStringMode operator^(StatusToStringMode lhs,
                                              StatusToStringMode rhs) {
  return static_cast<StatusToStringMode>(static_cast<int>(lhs) ^
                                         static_cast<int>(rhs));
}
inline constexpr StatusToStringMode operator~(StatusToStringMode arg) {
  return static_cast<StatusToStringMode>(~static_cast<int>(arg));
}
inline StatusToStringMode& operator&=(StatusToStringMode& lhs,
                                      StatusToStringMode rhs) {
  lhs = lhs & rhs;
  return lhs;
}
inline StatusToStringMode& operator|=(StatusToStringMode& lhs,
                                      StatusToStringMode rhs) {
  lhs = lhs | rhs;
  return lhs;
}
inline StatusToStringMode& operator^=(StatusToStringMode& lhs,
                                      StatusToStringMode rhs) {
  lhs = lhs ^ rhs;
  return lhs;
}

// turbo::Status
//
// The `turbo::Status` class is generally used to gracefully handle errors
// across API boundaries (and in particular across RPC boundaries). Some of
// these errors may be recoverable, but others may not. Most
// functions which can produce a recoverable error should be designed to return
// either an `turbo::Status` (or the similar `turbo::ResultStatus<T>`, which holds
// either an object of type `T` or an error).
//
// API developers should construct their functions to return `turbo::OkStatus()`
// upon success, or an `turbo::StatusCode` upon another type of error (e.g
// an `turbo::StatusCode::kInvalidArgument` error). The API provides convenience
// functions to construct each status code.
//
// Example:
//
// turbo::Status myFunction(std::string_view fname, ...) {
//   ...
//   // encounter error
//   if (error condition) {
//     // Construct an turbo::StatusCode::kInvalidArgument error
//     return turbo::InvalidArgumentError("bad mode");
//   }
//   // else, return OK
//   return turbo::OkStatus();
// }
//
// Users handling status error codes should prefer checking for an OK status
// using the `ok()` member function. Handling multiple error codes may justify
// use of switch statement, but only check for error codes you know how to
// handle; do not try to exhaustively match against all canonical error codes.
// Errors that cannot be handled should be logged and/or propagated for higher
// levels to deal with. If you do use a switch statement, make sure that you
// also provide a `default:` switch case, so that code does not break as other
// canonical codes are added to the API.
//
// Example:
//
//   turbo::Status result = DoSomething();
//   if (!result.ok()) {
//     TURBO_LOG(ERROR) << result;
//   }
//
//   // Provide a default if switching on multiple error codes
//   switch (result.code()) {
//     // The user hasn't authenticated. Ask them to reauth
//     case turbo::StatusCode::kUnauthenticated:
//       DoReAuth();
//       break;
//     // The user does not have permission. Log an error.
//     case turbo::StatusCode::kPermissionDenied:
//       TURBO_LOG(ERROR) << result;
//       break;
//     // Propagate the error otherwise.
//     default:
//       return true;
//   }
//
// An `turbo::Status` can optionally include a payload with more information
// about the error. Typically, this payload serves one of several purposes:
//
//   * It may provide more fine-grained semantic information about the error to
//     facilitate actionable remedies.
//   * It may provide human-readable contexual information that is more
//     appropriate to display to an end user.
//
// Example:
//
//   turbo::Status result = DoSomething();
//   // Inform user to retry after 30 seconds
//   // See more error details in googleapis/google/rpc/error_details.proto
//   if (turbo::IsResourceExhausted(result)) {
//     google::rpc::RetryInfo info;
//     info.retry_delay().seconds() = 30;
//     // Payloads require a unique key (a URL to ensure no collisions with
//     // other payloads), and an `turbo::Cord` to hold the encoded data.
//     std::string_view url = "type.googleapis.com/google.rpc.RetryInfo";
//     result.SetPayload(url, info.SerializeAsCord());
//     return result;
//   }
//
// For documentation see https://abseil.io/docs/cpp/guides/status.
//
// Returned Status objects may not be ignored. status_internal.h has a forward
// declaration of the form
// class TURBO_MUST_USE_RESULT Status;
class Status final {
 public:
  // Constructors

  // This default constructor creates an OK status with no message or payload.
  // Avoid this constructor and prefer explicit construction of an OK status
  // with `turbo::OkStatus()`.
  Status();

  // Creates a status in the canonical error space with the specified
  // `turbo::StatusCode` and error message.  If `code == turbo::StatusCode::kOk`,  // NOLINT
  // `msg` is ignored and an object identical to an OK status is constructed.
  //
  // The `msg` string must be in UTF-8. The implementation may complain (e.g.,  // NOLINT
  // by printing a warning) if it is not.
  Status(turbo::StatusCode code, std::string_view msg);

  Status(unsigned short int index, turbo::StatusCode code, std::string_view msg);

  /*
  template <typename... Args>
  Status(unsigned short int module_index, turbo::StatusCode code, const FormatSpec<Args...>& format,
         const Args&... args);
         */
  Status(const Status&);
  Status& operator=(const Status& x);

  // Move operators

  // The moved-from state is valid but unspecified.
  Status(Status&&) noexcept;
  Status& operator=(Status&&);

  ~Status();

  // Status::Update()
  //
  // Updates the existing status with `new_status` provided that `this->ok()`.
  // If the existing status already contains a non-OK error, this update has no
  // effect and preserves the current data. Note that this behavior may change
  // in the future to augment a current non-ok status with additional
  // information about `new_status`.
  //
  // `Update()` provides a convenient way of keeping track of the first error
  // encountered.
  //
  // Example:
  //   // Instead of "if (overall_status.ok()) overall_status = new_status"
  //   overall_status.Update(new_status);
  //
  void Update(const Status& new_status);
  void Update(Status&& new_status);

  // Status::ok()
  //
  // Returns `true` if `this->code()` == `turbo::StatusCode::kOk`,
  // indicating the absence of an error.
  // Prefer checking for an OK status using this member function.
  TURBO_MUST_USE_RESULT bool ok() const;

  // Status::code()
  //
  // Returns the canonical error code of type `turbo::StatusCode` of this status.
  turbo::StatusCode code() const;

  // Status::raw_code()
  //
  // Returns a raw (canonical) error code corresponding to the enum value of
  // `google.rpc.Code` definitions within
  // https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto.
  // These values could be out of the range of canonical `turbo::StatusCode`
  // enum values.
  //
  // NOTE: This function should only be called when converting to an associated
  // wire format. Use `Status::code()` for error handling.
  int raw_code() const;

  unsigned short int index() const;

  // Status::message()
  //
  // Returns the error message associated with this error code, if available.
  // Note that this message rarely describes the error code.  It is not unusual
  // for the error message to be the empty string. As a result, prefer
  // `operator<<` or `Status::ToString()` for debug logging.
  std::string_view message() const;

  friend bool operator==(const Status&, const Status&);
  friend bool operator!=(const Status&, const Status&);

  // Status::ToString()
  //
  // Returns a string based on the `mode`. By default, it returns combination of
  // the error code name, the message and any associated payload messages. This
  // string is designed simply to be human readable and its exact format should
  // not be load bearing. Do not depend on the exact format of the result of
  // `ToString()` which is subject to change.
  //
  // The printed code name and the message are generally substrings of the
  // result, and the payloads to be printed use the status payload printer
  // mechanism (which is internal).
  std::string ToString(
      StatusToStringMode mode = StatusToStringMode::kDefault) const;

  // Status::IgnoreError()
  //
  // Ignores any errors. This method does nothing except potentially suppress
  // complaints from any tools that are checking that errors are not dropped on
  // the floor.
  void IgnoreError() const;

  // swap()
  //
  // Swap the contents of one status with another.
  friend void swap(Status& a, Status& b);

  //----------------------------------------------------------------------------
  // Payload Management APIs
  //----------------------------------------------------------------------------

  // A payload may be attached to a status to provide additional context to an
  // error that may not be satisfied by an existing `turbo::StatusCode`.
  // Typically, this payload serves one of several purposes:
  //
  //   * It may provide more fine-grained semantic information about the error
  //     to facilitate actionable remedies.
  //   * It may provide human-readable contexual information that is more
  //     appropriate to display to an end user.
  //
  // A payload consists of a [key,value] pair, where the key is a string
  // referring to a unique "type URL" and the value is an object of type
  // `turbo::Cord` to hold the contextual data.
  //
  // The "type URL" should be unique and follow the format of a URL
  // (https://en.wikipedia.org/wiki/URL) and, ideally, provide some
  // documentation or schema on how to interpret its associated data. For
  // example, the default type URL for a protobuf message type is
  // "type.googleapis.com/packagename.messagename". Other custom wire formats
  // should define the format of type URL in a similar practice so as to
  // minimize the chance of conflict between type URLs.
  // Users should ensure that the type URL can be mapped to a concrete
  // C++ type if they want to deserialize the payload and read it effectively.
  //
  // To attach a payload to a status object, call `Status::SetPayload()`,
  // passing it the type URL and an `turbo::Cord` of associated data. Similarly,
  // to extract the payload from a status, call `Status::GetPayload()`. You
  // may attach multiple payloads (with differing type URLs) to any given
  // status object, provided that the status is currently exhibiting an error
  // code (i.e. is not OK).

  // Status::GetPayload()
  //
  // Gets the payload of a status given its unique `type_url` key, if present.
  std::optional<turbo::Cord> GetPayload(std::string_view type_url) const;

  // Status::SetPayload()
  //
  // Sets the payload for a non-ok status using a `type_url` key, overwriting
  // any existing payload for that `type_url`.
  //
  // NOTE: This function does nothing if the Status is ok.
  void SetPayload(std::string_view type_url, turbo::Cord payload);

  // Status::ErasePayload()
  //
  // Erases the payload corresponding to the `type_url` key.  Returns `true` if
  // the payload was present.
  bool ErasePayload(std::string_view type_url);

  // Status::ForEachPayload()
  //
  // Iterates over the stored payloads and calls the
  // `visitor(type_key, payload)` callable for each one.
  //
  // NOTE: The order of calls to `visitor()` is not specified and may change at
  // any time.
  //
  // NOTE: Any mutation on the same 'turbo::Status' object during visitation is
  // forbidden and could result in undefined behavior.
  void ForEachPayload(
      turbo::FunctionRef<void(std::string_view, const turbo::Cord&)> visitor)
      const;

 private:
  friend Status CancelledError();

  // Creates a status in the canonical error space with the specified
  // code, and an empty error message.
  explicit Status(turbo::StatusCode code);

  static void UnrefNonInlined(uintptr_t rep);
  static void Ref(uintptr_t rep);
  static void Unref(uintptr_t rep);

  // REQUIRES: !ok()
  // Ensures rep_ is not shared with any other Status.
  void PrepareToModify();

  const status_internal::Payloads* GetPayloads() const;
  status_internal::Payloads* GetPayloads();

  static bool EqualsSlow(const turbo::Status& a, const turbo::Status& b);

  // MSVC 14.0 limitation requires the const.
  static constexpr const char kMovedFromString[] =
      "Status accessed after move.";

  static const std::string* EmptyString();
  static const std::string* MovedFromString();

  // Returns whether rep contains an inlined representation.
  // See rep_ for details.
  static bool IsInlined(uintptr_t rep);

  // Indicates whether this Status was the rhs of a move operation. See rep_
  // for details.
  static bool IsMovedFrom(uintptr_t rep);
  static uintptr_t MovedFromRep();

  // Convert between error::Code and the inlined uintptr_t representation used
  // by rep_. See rep_ for details.
  static uintptr_t CodeToInlinedRep(turbo::StatusCode code);
  static uintptr_t CodeToInlinedRep(unsigned short int module_index, turbo::StatusCode code);

  static turbo::StatusCode InlinedRepToCode(uintptr_t rep);
  static unsigned short int InlinedRepToIndex(uintptr_t rep);

  // Converts between StatusRep* and the external uintptr_t representation used
  // by rep_. See rep_ for details.
  static uintptr_t PointerToRep(status_internal::StatusRep* r);
  static status_internal::StatusRep* RepToPointer(uintptr_t r);

  std::string ToStringSlow(StatusToStringMode mode) const;

  // Status supports two different representations.
  //  - When the low bit is off it is an inlined representation.
  //    It uses the canonical error space, no message or payload.
  //    The error code is (rep_ >> 2).
  //    The (rep_ & 2) bit is the "moved from" indicator, used in IsMovedFrom().
  //  - When the low bit is on it is an external representation.
  //    In this case all the data comes from a heap allocated Rep object.
  //    (rep_ - 1) is a status_internal::StatusRep* pointer to that structure.
  uintptr_t rep_;
};

// OkStatus()
//
// Returns an OK status, equivalent to a default constructed instance. Prefer
// usage of `turbo::OkStatus()` when constructing such an OK status.
Status OkStatus();

// operator<<()
//
// Prints a human-readable representation of `x` to `os`.
std::ostream& operator<<(std::ostream& os, const Status& x);

// IsAborted()
// IsAlreadyExists()
// IsCancelled()
// IsDataLoss()
// IsDeadlineExceeded()
// IsFailedPrecondition()
// IsInternal()
// IsInvalidArgument()
// IsNotFound()
// IsOutOfRange()
// IsPermissionDenied()
// IsResourceExhausted()
// IsUnauthenticated()
// IsUnavailable()
// IsUnimplemented()
// IsUnknown()
//
// These convenience functions return `true` if a given status matches the
// `turbo::StatusCode` error code of its associated function.
TURBO_MUST_USE_RESULT bool IsAborted(const Status& status);
TURBO_MUST_USE_RESULT bool IsAlreadyExists(const Status& status);
TURBO_MUST_USE_RESULT bool IsCancelled(const Status& status);
TURBO_MUST_USE_RESULT bool IsDataLoss(const Status& status);
TURBO_MUST_USE_RESULT bool IsDeadlineExceeded(const Status& status);
TURBO_MUST_USE_RESULT bool IsFailedPrecondition(const Status& status);
TURBO_MUST_USE_RESULT bool IsInternal(const Status& status);
TURBO_MUST_USE_RESULT bool IsInvalidArgument(const Status& status);
TURBO_MUST_USE_RESULT bool IsNotFound(const Status& status);
TURBO_MUST_USE_RESULT bool IsOutOfRange(const Status& status);
TURBO_MUST_USE_RESULT bool IsPermissionDenied(const Status& status);
TURBO_MUST_USE_RESULT bool IsResourceExhausted(const Status& status);
TURBO_MUST_USE_RESULT bool IsUnauthenticated(const Status& status);
TURBO_MUST_USE_RESULT bool IsUnavailable(const Status& status);
TURBO_MUST_USE_RESULT bool IsUnimplemented(const Status& status);
TURBO_MUST_USE_RESULT bool IsUnknown(const Status& status);

// AbortedError()
// AlreadyExistsError()
// CancelledError()
// DataLossError()
// DeadlineExceededError()
// FailedPreconditionError()
// InternalError()
// InvalidArgumentError()
// NotFoundError()
// OutOfRangeError()
// PermissionDeniedError()
// ResourceExhaustedError()
// UnauthenticatedError()
// UnavailableError()
// UnimplementedError()
// UnknownError()
//
// These convenience functions create an `turbo::Status` object with an error
// code as indicated by the associated function name, using the error message
// passed in `message`.
Status AbortedError(std::string_view message);
Status AlreadyExistsError(std::string_view message);
Status CancelledError(std::string_view message);
Status DataLossError(std::string_view message);
Status DeadlineExceededError(std::string_view message);
Status FailedPreconditionError(std::string_view message);
Status InternalError(std::string_view message);
Status InvalidArgumentError(std::string_view message);
Status NotFoundError(std::string_view message);
Status OutOfRangeError(std::string_view message);
Status PermissionDeniedError(std::string_view message);
Status ResourceExhaustedError(std::string_view message);
Status UnauthenticatedError(std::string_view message);
Status UnavailableError(std::string_view message);
Status UnimplementedError(std::string_view message);
Status UnknownError(std::string_view message);

// ErrnoToStatusCode()
//
// Returns the StatusCode for `error_number`, which should be an `errno` value.
// See https://en.cppreference.com/w/cpp/error/errno_macros and similar
// references.
turbo::StatusCode ErrnoToStatusCode(int error_number);

// ErrnoToStatus()
//
// Convenience function that creates a `turbo::Status` using an `error_number`,
// which should be an `errno` value.
Status ErrnoToStatus(int error_number, std::string_view message);

//------------------------------------------------------------------------------
// Implementation details follow
//------------------------------------------------------------------------------

inline Status::Status() : rep_(CodeToInlinedRep(turbo::kOk)) {}

inline Status::Status(turbo::StatusCode code) : rep_(CodeToInlinedRep(code)) {}

inline Status::Status(const Status& x) : rep_(x.rep_) { Ref(rep_); }

inline Status& Status::operator=(const Status& x) {
  uintptr_t old_rep = rep_;
  if (x.rep_ != old_rep) {
    Ref(x.rep_);
    rep_ = x.rep_;
    Unref(old_rep);
  }
  return *this;
}

inline Status::Status(Status&& x) noexcept : rep_(x.rep_) {
  x.rep_ = MovedFromRep();
}

inline Status& Status::operator=(Status&& x) {
  uintptr_t old_rep = rep_;
  if (x.rep_ != old_rep) {
    rep_ = x.rep_;
    x.rep_ = MovedFromRep();
    Unref(old_rep);
  }
  return *this;
}

inline void Status::Update(const Status& new_status) {
  if (ok()) {
    *this = new_status;
  }
}

inline void Status::Update(Status&& new_status) {
  if (ok()) {
    *this = std::move(new_status);
  }
}

inline Status::~Status() { Unref(rep_); }

inline bool Status::ok() const {
  return rep_ == CodeToInlinedRep(turbo::kOk);
}

inline std::string_view Status::message() const {
  return !IsInlined(rep_)
             ? RepToPointer(rep_)->message
             : (IsMovedFrom(rep_) ? std::string_view(kMovedFromString)
                                  : std::string_view());
}

inline bool operator==(const Status& lhs, const Status& rhs) {
  return lhs.rep_ == rhs.rep_ || Status::EqualsSlow(lhs, rhs);
}

inline bool operator!=(const Status& lhs, const Status& rhs) {
  return !(lhs == rhs);
}

inline std::string Status::ToString(StatusToStringMode mode) const {
  return ok() ? "OK" : ToStringSlow(mode);
}

inline void Status::IgnoreError() const {
  // no-op
}

inline void swap(turbo::Status& a, turbo::Status& b) {
  using std::swap;
  swap(a.rep_, b.rep_);
}

inline const status_internal::Payloads* Status::GetPayloads() const {
  return IsInlined(rep_) ? nullptr : RepToPointer(rep_)->payloads.get();
}

inline status_internal::Payloads* Status::GetPayloads() {
  return IsInlined(rep_) ? nullptr : RepToPointer(rep_)->payloads.get();
}

inline bool Status::IsInlined(uintptr_t rep) { return (rep & 1) == 0; }

inline bool Status::IsMovedFrom(uintptr_t rep) {
  return IsInlined(rep) && (rep & 2) != 0;
}

inline uintptr_t Status::MovedFromRep() {
  return CodeToInlinedRep(turbo::kInternal) | 2;
}

inline uintptr_t Status::CodeToInlinedRep(turbo::StatusCode code) {
  return static_cast<uintptr_t>(code) << 2;
}

inline uintptr_t Status::CodeToInlinedRep(unsigned short int module_index, turbo::StatusCode code) {
    uintptr_t  ret =  static_cast<uintptr_t>(module_index)<<32;
    ret |=  static_cast<uintptr_t>(code);
    return ret << 2;
}

inline turbo::StatusCode Status::InlinedRepToCode(uintptr_t rep) {
  assert(IsInlined(rep));
  static constexpr uintptr_t kCodeMask = 0x00000000FFFFFFFF;
  return static_cast<turbo::StatusCode>((rep >> 2) & kCodeMask);
}
inline unsigned short int Status::InlinedRepToIndex(uintptr_t rep) {
    assert(IsInlined(rep));
    static constexpr uintptr_t kIndexMask = 0x000000000000FFFF;
    return static_cast<unsigned short int>((rep >> 34) & kIndexMask);
}
inline status_internal::StatusRep* Status::RepToPointer(uintptr_t rep) {
  assert(!IsInlined(rep));
  return reinterpret_cast<status_internal::StatusRep*>(rep - 1);
}

inline uintptr_t Status::PointerToRep(status_internal::StatusRep* rep) {
  return reinterpret_cast<uintptr_t>(rep) + 1;
}

inline void Status::Ref(uintptr_t rep) {
  if (!IsInlined(rep)) {
    RepToPointer(rep)->ref.fetch_add(1, std::memory_order_relaxed);
  }
}

inline void Status::Unref(uintptr_t rep) {
  if (!IsInlined(rep)) {
    UnrefNonInlined(rep);
  }
}

inline Status OkStatus() { return Status(); }

// Creates a `Status` object with the `turbo::StatusCode::kCancelled` error code
// and an empty message. It is provided only for efficiency, given that
// message-less kCancelled errors are common in the infrastructure.
inline Status CancelledError() { return Status(turbo::kCancelled); }

TURBO_NAMESPACE_END
}  // namespace turbo

#endif  // TURBO_BASE_STATUS_H_
