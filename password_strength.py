import getpass


def is_case_sensitive(password):
    return (not password.isupper()) and \
           (not password.islower()) and \
           (not password.isnumeric())


def contains_numerals(password):
    result = False
    for numeral in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        result = result or (password.find(numeral) != -1)
    return result


def contains_letters(password):
    return password.upper() != password.lower()


def contains_special_chars(password):
    special_chars_string = '" !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"'
    result = False
    for char in special_chars_string:
        result = result or password.find(char) != -1
    return result


def is_very_long(password):
    return len(password) >= 20


def is_long(password):
    return len(password) >= 12


def is_short(password):
    return len(password) <= 6


def is_in_the_blacklist(password):
    blacklist = [
        'qwerty',
        'password',
        'football',
        'princess',
        'login',
        'welcome',
        'solo',
        'admin',
        'flower',
        'dragon',
        'sunshine',
        'master',
        'hottie',
        'love',
        'monkey',
        'baseball',
        'ashley',
        'bailey',
        'shadow',
        'superman',
        'mustang',
        'google',
        'facebook'
    ]
    return password.lower() in blacklist


def get_password_strength(password):
    if is_in_the_blacklist(password) or is_short(password):
        return 1

    if is_very_long(password):
        result = 3
    elif is_long(password):
        result = 2
    else:
        result = 1
    result += int(is_case_sensitive(password)) * 2
    result += int(contains_numerals(password) and contains_letters(password)) * 2
    result += int(contains_numerals(password) and contains_special_chars(password)) * 2
    result += int(contains_letters(password) and contains_special_chars(password)) * 2
    return result if result < 10 else 10


if __name__ == '__main__':
    password = getpass.getpass(prompt='Enter a password to analyze: ')
    print('The password strength is ' + str(get_password_strength(password)) + ' point out of 10')
