import codewars_test as test
from solution.multiply import multiply


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multiply(2, 1), 2)
