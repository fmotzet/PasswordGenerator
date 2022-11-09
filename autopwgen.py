import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!#$%()-=+'
number = '0123456789'

def password_generator( length = 18, lowerbool = 1, upperbool = 1, sybolsbool = 1, numberbool = 1):

    # print("length, lowercase_letters, uppercase_letters, symbols, numbers")
    print('py  -c \'import pwgen; pwgen.password_generator()\'')
    passwordchars = ''

    if lowerbool:
        passwordchars += lower
    if upperbool:
        passwordchars += upper
    if sybolsbool:
        passwordchars += symbols
    if numberbool:
        passwordchars += number

    password = ''
    for x in range(length+1):
        password = ''.join([password, random.choice(passwordchars)])       
    print(password)
    return ''

password_generator()
