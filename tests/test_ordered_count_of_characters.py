import codewars_test as test  # https://github.com/codewars/python-test-framework
import add_parent_folder_to_sys_path
from solution.kyu_7.ordered_count_of_characters import ordered_count


test.describe("Basic Tests")

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    test.assert_equals(ordered_count(inp), exp)
