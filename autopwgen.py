import random
import pprint as pp

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
symbols = '!#$%()=+'
number = '0123456789'
number_of_pws = 50 

# print("length, lowercase_letters, uppercase_letters, symbols, numbers")
print("Custom Generator:")
print('py  -c \'import pwgen; pwgen.password_generator()\'\n')

def dash_adder(string, x):

    paword = ''
    cnt = 0
    for ch in string:
        if cnt % x == 0 and cnt != 0:  # checking if cnt is a multiple of x and not 0, we don't want to put dash at index 0
            paword += '-'
        cnt += 1
        paword += ch
    return paword


def password_generator():

    passwordchars = ''
    passwordchars += lower
    passwordchars += upper
    #passwordchars += symbols
    passwordchars += number

    password = ''
    for x in range(20):
        password = ''.join([password, random.choice(passwordchars)])
    
    
    
    if len(password) > 10:
        if len(password) % 5 == 0:
            return dash_adder(password, 5)
        if len(password) % 6 == 0:
            return dash_adder(password, 6)
        if len(password) % 4 == 0:
            return dash_adder(password, 4)
        return dash_adder(password, 5)

#gen mre than 1 password 
list_of_pws = []

while len(list_of_pws) < number_of_pws:
    list_of_pws.append(password_generator())

pp.pprint(list_of_pws,width=150,compact=True)
