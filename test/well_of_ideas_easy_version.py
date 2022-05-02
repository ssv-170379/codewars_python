import codewars_test as test
from solution.well_of_ideas_easy_version import well


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')
