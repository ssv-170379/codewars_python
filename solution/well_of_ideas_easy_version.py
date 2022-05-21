"""
Well of Ideas - Easy Version
https://www.codewars.com/kata/57f222ce69e09c3630000212
"""
"""
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
"""


def well(x):
    goods = x.count('good')
    if goods == 0:
        return 'Fail!'
    elif goods <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'


if __name__ == '__main__':
    import codewars_test as test
    from solution.well_of_ideas_easy_version import well


    @test.describe("Fixed Tests")
    def fixed_tests():
        @test.it('Basic Test Cases')
        def basic_test_cases():
            test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
            test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
            test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')
