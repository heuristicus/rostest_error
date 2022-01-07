This is a tiny package which shows failure of rostest to show errors in the test scripts.

This seems to only be a problem when the instantiation of the unittest class fails. Errors in the actual code of test functions will display normally with a traceback.

Put the package into your catkin workspace, and build it

```commandline
catkin build rostest_example
```

The `test_error.py` test file has a deliberate error in it which will cause the test to return an error.

Run the test with

```commandline
catkin test rostest_example
```

The test result will be an error, but the cause of the error will not be displayed.

If the test is run with

```commandline
python3 test/test_error.py
```

With this, you will see the cause of the error, although without a traceback.