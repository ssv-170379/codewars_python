"""
IntroToArt
https://www.codewars.com/kata/5d7d05d070a6f60015c436d1
"""
"""
Help prepare for the entrance exams to art school.

It is known in advance that this year, the school chose the symmetric letter “W” as the object for the image, and the only condition for its image is only the size that is not known in advance, so as training, you need to come up with a way that accurately depicts the object.

Write a function that takes an integer and returns a list of strings with a line-by-line image of the object.

Below is an example function:

get_w(3) # should return:
[
'*   *   *',
' * * * * ',
'  *   *  '
]

get_w(5) # should return:
[
'*       *       *',
' *     * *     * ',
'  *   *   *   *  ',
'   * *     * *   ',
'    *       *    '
]

Return an empty list for height < 2.
"""


def get_w(height):
    width = (height * 4) - 3  # full width of 'w' drawing
    v_width = (width // 2)  # width of a single v-segment (actually overlapping 1 character)
    result = []
    if height >= 2:  # pass "Return an empty list for height < 2" condition
        for y in range(height):  # line_by_line
            line = ''
            segment_offs = 0  # start drawing leftmost 'v'
            for x in range(width):
                line += '*' if (x - segment_offs == y) or (x - segment_offs == v_width - y) else ' '
                if x == segment_offs + v_width:  # if x is beyond current segment
                    segment_offs += v_width  # proceed to the next v-segment
            result.append(line)
    return result


if __name__ == '__main__':
    import codewars_test as test
    from solution.intro_to_art import get_w


    @test.describe('Sample tests')
    def sample_tests():
        test.assert_equals(get_w(-5), [])
        test.assert_equals(get_w(1), [])
        test.assert_equals(get_w(3), [
            '*   *   *',
            ' * * * * ',
            '  *   *  '])
        test.assert_equals(get_w(7), [
            '*           *           *',
            ' *         * *         * ',
            '  *       *   *       *  ',
            '   *     *     *     *   ',
            '    *   *       *   *    ',
            '     * *         * *     ',
            '      *           *      '])
