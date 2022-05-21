"""
Closest and Smallest
https://www.codewars.com/kata/5868b2de442e3fb2bb000119
"""
"""
Input

    a string strng of n positive numbers (n = 0 or n >= 2)

Let us call weight of a number the sum of its digits. For example 99 will have "weight" 18, 100 will have "weight" 1.

Two numbers are "close" if the difference of their weights is small.
Task:

For each number in strng calculate its "weight" and then find two numbers of strng that have:

    the smallest difference of weights ie that are the closest
    with the smallest weights
    and with the smallest indices (or ranks, numbered from 0) in strng

Output:

    an array of two arrays, each subarray in the following format:

[number-weight, index in strng of the corresponding number, original corresponding number in strng]

or a pair of two subarrays (Haskell, Clojure, FSharp) or an array of tuples (Elixir, C++)

or a (char*) in C or a string in some other languages mimicking an array of two subarrays or a string

or a matrix in R (2 rows, 3 columns, no columns names)

The two subarrays are sorted in ascending order by their number weights if these weights are different, by their indexes in the string if they have the same weights.
Examples:

Let us call that function closest

strng = "103 123 4444 99 2000"
the weights are 4, 6, 16, 18, 2 (ie 2, 4, 6, 16, 18)

closest should return [[2, 4, 2000], [4, 0, 103]] (or ([2, 4, 2000], [4, 0, 103])
or [{2, 4, 2000}, {4, 0, 103}] or ... depending on the language)
because 2000 and 103 have for weight 2 and 4, their indexes in strng are 4 and 0.
The smallest difference is 2.
4 (for 103) and 6 (for 123) have a difference of 2 too but they are not 
the smallest ones with a difference of 2 between their weights.
....................

strng = "80 71 62 53"
All the weights are 8.
closest should return [[8, 0, 80], [8, 1, 71]]
71 and 62 have also:
- the smallest weights (which is 8 for all)
- the smallest difference of weights (which is 0 for all pairs)
- but not the smallest indices in strng.
....................

strng = "444 2000 445 544"
the weights are 12, 2, 13, 13 (ie 2, 12, 13, 13)

closest should return [[13, 2, 445], [13, 3, 544]] or ([13, 2, 445], [13, 3, 544])
or [{13, 2, 445}, {13, 3, 544}] or ...
444 and 2000 have the smallest weights (12 and 2) but not the smallest difference of weights;
they are not the closest.
Here the smallest difference is 0 and in the result the indexes are in ascending order.
...................

closest("444 2000 445 644 2001 1002") --> [[3, 4, 2001], [3, 5, 1002]] or ([3, 4, 2001], 
[3, 5, 1002]]) or [{3, 4, 2001}, {3, 5, 1002}] or ...
Here the smallest difference is 0 and in the result the indexes are in ascending order.
...................

closest("239382 162 254765 182 485944 468751 49780 108 54")
The weights are: 27, 9, 29, 11, 34, 31, 28, 9, 9.
closest should return  [[9, 1, 162], [9, 7, 108]] or ([9, 1, 162], [9, 7, 108]) 
or [{9, 1, 162}, {9, 7, 108}] or ...
108 and 54 have the smallest difference of weights too, they also have 
the smallest weights but they don't have the smallest ranks in the original string.
..................

closest("54 239382 162 254765 182 485944 468751 49780 108")
closest should return  [[9, 0, 54], [9, 2, 162]] or ([9, 0, 54], [9, 2, 162])
or [{9, 0, 54}, {9, 2, 162}] or ...

Notes :

If n == 0 closest("") should return []

    or ([], []) in Haskell, Clojure, FSharp

    or [{}, {}] in Elixir or '(() ()) in Racket

    or {{0,0,0}, {0,0,0}} in C++

    or "[(), ()]" in Go, Nim,

    or "{{0,0,0}, {0,0,0}}" in C, NULL in R

    or "" in Perl.

See Example tests for the format of the results in your language.
"""


def closest(string: str) -> list:
    if not string:
        return []
    data = []
    for i, item in enumerate(string.split()):  # index input data
        data.append({'number': int(item),
                     'weight': sum(map(int, item)),
                     'index': i})

    data = sorted(data, key=lambda x: (x['weight'], x['index']))  # sort by weight(primary) and index(secondary) ascending

    distances = [x2['weight'] - x1['weight'] for x1, x2 in zip(data, data[1:])]  # distances between all adjacent elements
    min_dist_index = distances.index(min(distances))  # index of the first element of the pair with minimal distance
    first_closest_pair = data[min_dist_index:min_dist_index + 2]  # the first pair of elements with the closest range in data
    return [[x['weight'], x['index'], x['number']] for x in first_closest_pair]  # [[weight1, index1, number1], [weight2, index2, number2]] of the pair found


if __name__ == '__main__':
    import codewars_test as test


    def _testing(actual, expected):
        test.assert_equals(actual, expected)


    test.describe("closest")
    test.it("Basic tests")
    _testing(closest(""), [])
    _testing(closest("103 123 4444 99 2000 "), [[2, 4, 2000], [4, 0, 103]])
    _testing(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"), [[13, 9, 85], [14, 3, 176]])
    _testing(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"), [[8, 5, 134], [8, 7, 62]])
    _testing(closest("241259 154 155206 194 180502 147 300751 200 406683 37 57"), [[10, 1, 154], [10, 9, 37]])
    _testing(closest("89998 187 126159 175 338292 89 39962 145 394230 167 1"), [[13, 3, 175], [14, 9, 167]])

    _testing(closest("403749 18 278325 97 304194 119 58359 165 144403 128 38"), [[11, 5, 119], [11, 9, 128]])
    _testing(closest("28706 196 419018 130 49183 124 421208 174 404307 60 24"), [[6, 9, 60], [6, 10, 24]])
    _testing(closest("189437 110 263080 175 55764 13 257647 53 486111 27 66"), [[8, 7, 53], [9, 9, 27]])
    _testing(closest("79257 160 44641 146 386224 147 313622 117 259947 155 58"), [[11, 3, 146], [11, 9, 155]])
    _testing(closest("315411 165 53195 87 318638 107 416122 121 375312 193 59"), [[15, 0, 315411], [15, 3, 87]])
