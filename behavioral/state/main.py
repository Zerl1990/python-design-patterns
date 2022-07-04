from behavioral.state.test_runner import TestRunner

if __name__ == "__main__":
    runner = TestRunner()
    runner.start()
    runner.run()
    runner.success()
