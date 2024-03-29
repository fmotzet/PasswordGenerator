import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!#$%()=+'
number = '0123456789'


def dash_adder(string, x):

    paword = ''
    cnt = 0
    for char in string:
        if cnt % x == 0 and cnt != 0:  # checking if cnt is a multiple of x and not 0, we don't want to put dash at index 0
            paword += '-'
        cnt += 1
        paword += char
    return paword


def password_generator(length=18, dashesbool=1, lowerbool=1, upperbool=1, symbolbool=1, numberbool=1):

    print("length, dashes, lowercase_letters, uppercase_letters, symbols, numbers")
    passwordchars = ''

    # if all are false
    if (lowerbool + upperbool + symbolbool + numberbool) == 0:
        return "Error no symbols selected"

    if lowerbool:
        passwordchars += lower
    if upperbool:
        passwordchars += upper
    if symbolbool:
        passwordchars += symbols
    if numberbool:
        passwordchars += number
    password = ''

    for x in range(length):
        password = ''.join([password, random.choice(passwordchars)])

    if dashesbool and (len(password) > 10):
        if len(password) % 5 == 0:
            password = dash_adder(password, 5)
        elif len(password) % 6 == 0:
            password = dash_adder(password, 6)
        elif len(password) % 4 == 0:
            password = dash_adder(password, 4)
        password = dash_adder(password, 5)
    print(password)
    return password
