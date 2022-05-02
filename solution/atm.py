"""
ATM
https://www.codewars.com/kata/5635e7cb49adc7b54500001c
"""
"""
An ATM has banknotes of nominal values 10, 20, 50, 100, 200 and 500 dollars. You can consider that there is a large enough supply of each of these banknotes.

You have to write the ATM's function that determines the minimal number of banknotes needed to honor a withdrawal of n dollars, with 1 <= n <= 1500.

Return that number, or -1 if it is impossible.

Good Luck!!!
"""


def solve(withdrawal):
    nominals = (500, 200, 100, 50, 20, 10)  # descending order
    if withdrawal % nominals[-1]:
        return -1  # desired withdrawal is not a multiple of minimal nominal, cannot give this amount, return -1
    notes_count = 0
    for nominal in nominals:  # iterate in descending order
        notes, reminder = divmod(withdrawal, nominal)  # divmod returns // (floor div, how many notes are in the sum) and % (reminder, how much of the withdrawal remains without those notes)
        notes_count += notes  # add notes count
        withdrawal = reminder  # decrease withdrawal by the value of counted notes
        if not withdrawal:  # to speed up process and not iterate over lesser nominals if withdrawal reminder is already 0
            break

    return notes_count
