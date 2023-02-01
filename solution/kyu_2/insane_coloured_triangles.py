"""
Insane Coloured Triangles
https://www.codewars.com/kata/5a331ea7ee1aae8f24000175
"""
"""
Disclaimer

This Kata is an insane step-up from Avanta's Kata (https://www.codewars.com/kata/coloured-triangles), so I recommend to solve it first before trying this one.

Problem Description

A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.

For example, different possibilities are:

Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G

With a bigger example:

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G

You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would be given 'RRGBRGBB', and you should return 'G'.
Constraints

1 <= length(row) <= 10 ** 5

The input string will only contain the uppercase letters 'B', 'G' or 'R'.

The exact number of test cases will be as follows:

    100 tests of 100 <= length(row) <= 1000
    100 tests of 1000 <= length(row) <= 10000
    100 tests of 10000 <= length(row) <= 100000

Examples

triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
"""

boil_down = {
    ('R', 'R'): 'R',
    ('G', 'G'): 'G',
    ('B', 'B'): 'B',
    ('B', 'G'): 'R',
    ('G', 'B'): 'R',
    ('B', 'R'): 'G',
    ('R', 'B'): 'G',
    ('G', 'R'): 'B',
    ('R', 'G'): 'B',
}

"""
Main insight behind this solution is:
There are triangles of a certain sizes that can be solved (calculated final color at the bottom) in one go by just analyzing two points at the ends of the upper row
"""


def get_fast_lengths(row):
    """Return all sizes of fast-solvable triangles within the length of the input row"""
    fast_sizes = []
    size = 2
    while size <= len(row):
        fast_sizes.append(size)
        size = (size * 3) - 2  # 2, 4, 10, 28, 82, 244, 730...
    return fast_sizes


def triangle(row: str) -> str:
    fast_sizes = get_fast_lengths(row)  # find all fast-solvable triangle sizes within the length of the row
    while len(row) > 1:  # row contains multiple elements
        fast_size = [f for f in fast_sizes if f <= len(row)][-1]  # pick biggest fast-solvable triangle size that fits in the row
        row = [
            boil_down[(row[i], row[i + fast_size - 1])]
            for i in range(len(row) - fast_size + 1)
        ]  # calculate row {fast_size - 1} lines below current by solving all possible fast-triangles of the current row
    return row[0]  # return the only value left
