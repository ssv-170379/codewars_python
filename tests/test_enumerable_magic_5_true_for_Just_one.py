import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.enumerable_magic_5_true_for_Just_one import one


@test.describe('Example Tests')
def example_tests():
    equals_9 = lambda x: x == 9
    less_than_9 = lambda x: x < 9
    greater_than_9 = lambda x: x > 9
    arr = (6, 7, 8, 9, 10, 11)

    test.assert_equals(one(arr, equals_9), True)
    test.assert_equals(one(arr, less_than_9), False)
    test.assert_equals(one(arr, greater_than_9), False)
