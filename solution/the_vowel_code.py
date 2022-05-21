"""
The Vowel Code
https://www.codewars.com/kata/53697be005f803751e0015aa
"""
"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
"""

tr_schema = ('aeiou', '12345')
encode_table = str.maketrans(tr_schema[0], tr_schema[1])
decode_table = str.maketrans(tr_schema[1], tr_schema[0])


def encode(st: str):
    return st.translate(encode_table)


def decode(st):
    return st.translate(decode_table)


if __name__ == '__main__':
    import codewars_test as test

    test.assert_equals(encode('hello'), 'h2ll4')
    test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
    test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
    test.assert_equals(decode('h2ll4'), 'hello')
