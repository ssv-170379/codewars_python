"""
Disemvowel Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e
"""
"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

import re


def disemvowel(string: str):
    return re.sub('[aoieu]', '', string, flags=re.IGNORECASE)


if __name__ == '__main__':
    import codewars_test as test
    from solution.disemvowel_trolls import disemvowel

    test.assert_equals(disemvowel("This website is for losers LOL!"),
                       "Ths wbst s fr lsrs LL!")
