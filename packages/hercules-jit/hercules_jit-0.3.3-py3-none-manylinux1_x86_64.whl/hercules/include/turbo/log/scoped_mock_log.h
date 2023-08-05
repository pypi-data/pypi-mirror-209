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
// File: log/scoped_mock_log.h
// -----------------------------------------------------------------------------
//
// This header declares `class turbo::ScopedMockLog`, for use in testing.

#ifndef TURBO_LOG_SCOPED_MOCK_LOG_H_
#define TURBO_LOG_SCOPED_MOCK_LOG_H_

#include <atomic>
#include <string>

#include "turbo/base/log_severity.h"
#include "turbo/log/log_entry.h"
#include "turbo/log/log_sink.h"
#include "turbo/platform/port.h"
#include "gmock/gmock.h"

namespace turbo {
TURBO_NAMESPACE_BEGIN

// MockLogDefault
//
// Controls how ScopedMockLog responds to unexpected calls by default.
enum class MockLogDefault { kIgnoreUnexpected, kDisallowUnexpected };

// ScopedMockLog
//
// ScopedMockLog is a LogSink that intercepts LOG() messages issued during its
// lifespan.
//
// Using this together with GoogleTest, it's easy to test how a piece of code
// calls LOG(). The typical usage, noting the distinction between
// "uninteresting" and "unexpected", looks like this:
//
//   using ::testing::_;
//   using ::testing::AnyNumber;
//   using ::testing::EndsWith;
//   using ::testing::kDoNotCaptureLogsYet;
//   using ::testing::Lt;
//
//   TEST(FooTest, LogsCorrectly) {
//     // Simple robust setup, ignores unexpected logs.
//     turbo::ScopedMockLog log;
//
//     // We expect the WARNING "Something bad!" exactly twice.
//     EXPECT_CALL(log, Log(turbo::LogSeverity::kWarning, _, "Something bad!"))
//         .Times(2);
//
//     // But we want no messages from foo.cc.
//     EXPECT_CALL(log, Log(_, EndsWith("/foo.cc"), _)).Times(0);
//
//     log.StartCapturingLogs();  // Call this after done setting expectations.
//     Foo();  // Exercises the code under test.
//   }
//
//   TEST(BarTest, LogsExactlyCorrectly) {
//     // Strict checking, fails for unexpected logs.
//     turbo::ScopedMockLog log(turbo::MockLogDefault::kDisallowUnexpected);
//
//     // ... but ignore low severity messages
//     EXPECT_CALL(log, Log(Lt(turbo::LogSeverity::kWarning), _, _))
//         .Times(AnyNumber());
//
//     // We expect the ERROR "Something bad!" exactly once.
//     EXPECT_CALL(log, Log(turbo::LogSeverity::kError, EndsWith("/foo.cc"),
//                 "Something bad!"))
//         .Times(1);
//
//     log.StartCapturingLogs();  // Call this after done setting expectations.
//     Bar();  // Exercises the code under test.
//    }
//
// Note that in a multi-threaded environment, all LOG() messages from a single
// thread will be handled in sequence, but that cannot be guaranteed for
// messages from different threads. In fact, if the same or multiple
// expectations are matched on two threads concurrently, their actions will be
// executed concurrently as well and may interleave.
class ScopedMockLog final {
 public:
  // ScopedMockLog::ScopedMockLog()
  //
  // Sets up the log and adds default expectations.
  explicit ScopedMockLog(
      MockLogDefault default_exp = MockLogDefault::kIgnoreUnexpected);
  ScopedMockLog(const ScopedMockLog&) = delete;
  ScopedMockLog& operator=(const ScopedMockLog&) = delete;

  // ScopedMockLog::~ScopedMockLog()
  //
  // Stops intercepting logs and destroys this ScopedMockLog.
  ~ScopedMockLog();

  // ScopedMockLog::StartCapturingLogs()
  //
  // Starts log capturing if the object isn't already doing so. Otherwise
  // crashes.
  //
  // Usually this method is called in the same thread that created this
  // ScopedMockLog. It is the user's responsibility to not call this method if
  // another thread may be calling it or StopCapturingLogs() at the same time.
  // It is undefined behavior to add expectations while capturing logs is
  // enabled.
  void StartCapturingLogs();

  // ScopedMockLog::StopCapturingLogs()
  //
  // Stops log capturing if the object is capturing logs. Otherwise crashes.
  //
  // Usually this method is called in the same thread that created this object.
  // It is the user's responsibility to not call this method if another thread
  // may be calling it or StartCapturingLogs() at the same time.
  //
  // It is UB to add expectations, while capturing logs is enabled.
  void StopCapturingLogs();

  // ScopedMockLog::UseAsLocalSink()
  //
  // Each `ScopedMockLog` is implemented with an `turbo::LogSink`; this method
  // returns a reference to that sink (e.g. for use with
  // `LOG(...).ToSinkOnly()`) and marks the `ScopedMockLog` as having been used
  // even if `StartCapturingLogs` is never called.
  turbo::LogSink& UseAsLocalSink();

  // Implements the mock method:
  //
  //   void Log(LogSeverity severity, std::string_view file_path,
  //            std::string_view message);
  //
  // The second argument to Log() is the full path of the source file in
  // which the LOG() was issued.
  //
  // This is a shorthand form, which should be used by most users. Use the
  // `Send` mock only if you want to add expectations for other log message
  // attributes.
  MOCK_METHOD(void, Log,
              (turbo::LogSeverity severity, const std::string& file_path,
               const std::string& message));

  // Implements the mock method:
  //
  //   void Send(const turbo::LogEntry& entry);
  //
  // This is the most generic form of mock that can be specified. Use this mock
  // only if you want to add expectations for log message attributes different
  // from the log message text, log message path and log message severity.
  //
  // If no expectations are specified for this mock, the default action is to
  // forward the call to the `Log` mock.
  MOCK_METHOD(void, Send, (const turbo::LogEntry&));

  // Implements the mock method:
  //
  //   void Flush();
  //
  // Use this mock only if you want to add expectations for log flush calls.
  MOCK_METHOD(void, Flush, ());

 private:
  class ForwardingSink final : public turbo::LogSink {
   public:
    explicit ForwardingSink(ScopedMockLog* sml) : sml_(sml) {}
    ForwardingSink(const ForwardingSink&) = delete;
    ForwardingSink& operator=(const ForwardingSink&) = delete;
    void Send(const turbo::LogEntry& entry) override { sml_->Send(entry); }
    void Flush() override { sml_->Flush(); }

   private:
    ScopedMockLog* sml_;
  };

  ForwardingSink sink_;
  bool is_capturing_logs_;
  std::atomic<bool> is_triggered_;
};

TURBO_NAMESPACE_END
}  // namespace turbo

#endif  // TURBO_LOG_SCOPED_MOCK_LOG_H_
