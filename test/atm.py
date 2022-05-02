import codewars_test as test
from solution.atm import solve

test.describe("solve")

test.it("should work when chosing notes is possible")
test.assert_equals(solve(770), 4, "Wrong result for 770")
test.assert_equals(solve(550), 2, "Wrong result for 550")
test.assert_equals(solve(10), 1, "Wrong result for 10")
test.assert_equals(solve(1250), 4, "Wrong result for 1250")
test.assert_equals(solve(1500), 3, "Wrong result for 1500")

test.it("should return -1 if chosing notes is not possible")
test.assert_equals(solve(125), -1, "Wrong result for 125")
test.assert_equals(solve(666), -1, "Wrong result for 666")
test.assert_equals(solve(42), -1, "Wrong result for 42")
