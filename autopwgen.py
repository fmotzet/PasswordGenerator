import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!#$%()=+'
number = '0123456789'

def dash_adder(string, x):

    paword = ''
    cnt = 0

    for ch in string:
        if cnt%x==0 and cnt!=0: # checking if cnt is a multiple of x and not 0, we don't want to put star at index 0
            paword += '-'
        cnt += 1
        paword += ch
    return paword


def password_generator():

    # print("length, lowercase_letters, uppercase_letters, symbols, numbers")
    print("Custom Generator:")
    print('py  -c \'import pwgen; pwgen.password_generator()\'\n')
    passwordchars = ''
    passwordchars += lower
    passwordchars += upper
    passwordchars += symbols
    passwordchars += number

    password = ''
    for x in range(20):
        password = ''.join([password, random.choice(passwordchars)])       
    print(dash_adder(password,5))
    return ''

password_generator()
