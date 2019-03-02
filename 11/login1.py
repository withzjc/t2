username = 'taibai'
password = '123'

i = 0
while  i<3:
    name = input('please enter your name :')
    pwd = input('please enter your password:')
    if username == name and password == pwd:
        print('success!')
        break
    else:
        print('fail,you have %d times'%(2-i))
        if (2-i) ==0:
            result = input('want try?')
            if result =="Yes":
                i = 0
                continue
    i += 1
else:print("buyaolian")