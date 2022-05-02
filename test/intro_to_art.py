import codewars_test as test
from solution.intro_to_art import get_w

@test.describe('Sample tests')
def sample_tests():
    test.assert_equals(get_w(-5),[])
    test.assert_equals(get_w(1),[])
    test.assert_equals(get_w(3),[
    '*   *   *',
    ' * * * * ',
    '  *   *  '])
    test.assert_equals(get_w(7),[
    '*           *           *',
    ' *         * *         * ',
    '  *       *   *       *  ',
    '   *     *     *     *   ',
    '    *   *       *   *    ',
    '     * *         * *     ',
    '      *           *      '])