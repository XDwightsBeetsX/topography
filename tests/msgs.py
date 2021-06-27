"""
Global Variables for Testing
"""

TEST_PREFIX = "[TESTS] -"

RUNNING = "RUNNING"
PASSED  = "PASSED"
FAILED  = "FAILED"


def running(methodName):
    print(f"{TEST_PREFIX} {methodName} - {RUNNING}")

def passed(methodName):
    print(f"{TEST_PREFIX} {methodName} - {PASSED}")

def failed(methodName, got, expected):
    print(f"{TEST_PREFIX} {methodName} - {FAILED} - got {got} but expected {expected}")
