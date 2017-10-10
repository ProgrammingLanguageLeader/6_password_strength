import getpass
import string


def is_case_sensitive(password):
    return not password.isupper() and \
           not password.islower() and \
           not password.isnumeric()


def contains_numerals(password):
    contains = False
    for char in password:
        contains = contains or char.isdigit()
    return contains


def contains_letters(password):
    return password.upper() != password.lower()


def contains_special_chars(password):
    special_chars_string = string.punctuation
    return any(char in password for char in special_chars_string)


def contains_numerals_and_letters(password):
    return contains_numerals(password) and contains_letters(password)


def contains_numerals_and_special_chars(password):
    return contains_numerals(password) and contains_special_chars(password)


def contains_letters_and_special_chars(password):
    return contains_letters(password) and contains_special_chars(password)


def is_very_long(password):
    return len(password) >= 20


def is_long(password):
    return len(password) >= 12


def is_short(password):
    return len(password) <= 6


def get_password_strength(password, blacklist):
    strength = 1
    if password in blacklist or is_short(password):
        return strength

    good_signs = {
        is_very_long: 3,
        is_long: 2,
        is_case_sensitive: 2,
        contains_numerals_and_letters: 2,
        contains_numerals_and_special_chars: 2,
        contains_letters_and_special_chars: 2
    }
    for good_sign, value in good_signs.items():
        strength += good_sign(password) * value
    return strength if strength < 10 else 10


def read_blacklist_from_file(filepath):
    try:
        with open(filepath, 'r') as blacklist_file:
            return blacklist_file.readlines()
    except IOError:
        return None
    

if __name__ == '__main__':
    password = getpass.getpass(prompt='Enter a password to analyze: ')
    blacklist = read_blacklist_from_file('blacklist.txt')
    if not blacklist:
        print('Check file "blacklist.txt"')
        exit(0)
    print(
        'The password strength is {} point out of 10'.format(
            get_password_strength(password, blacklist)
        )
    )
