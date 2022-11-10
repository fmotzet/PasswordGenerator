import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!#$%()=+'
number = '0123456789'
dashes = '-'


def dash_adder(string, x):

    paword = ''
    cnt = 0

    for ch in string:
        if cnt % x == 0 and cnt != 0:  # checking if cnt is a multiple of x and not 0, we don't want to put star at index 0
            paword += '-'
        cnt += 1
        paword += ch
    return paword


def password_generator(length=18, dashesbool=1, lowerbool=1, upperbool=1, sybolsbool=1, numberbool=1):

    print("length, dashes, lowercase_letters, uppercase_letters, symbols, numbers")
    passwordchars = ''

    # if all are false
    if (lowerbool + upperbool + sybolsbool + numberbool) == 0:
        return print("Yeah thats not gonna work my guy!")

    if lowerbool:
        passwordchars += lower
    if upperbool:
        passwordchars += upper
    if sybolsbool:
        passwordchars += symbols
    if numberbool:
        passwordchars += number
    password = ''

    for x in range(length):
        password = ''.join([password, random.choice(passwordchars)])

    if dashesbool and (len(password) > 10):
        # TODO Find good number of dashes
        print(dash_adder(password, 5))
        return ''
    print(password)
    return ''
