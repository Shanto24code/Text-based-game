answear = input('are you want to play this game? [yes/no]:')
if answear=='yes':
    print('welcome to our game')
    answear = input('do you want to go jungle or cave ?[jungle\cave]:')
    if answear=='jungle':
        print('you see a hungry tiger. the tiger will eat you .game closed.')
    elif answear=='cave':
        print('you see a bear front of you')
        answear = input('what should you do run or fight :')
    if answear=='fight':
        print('bear is too much strong . you lose the fight and also you lose the game')
    else:
        print('wow you still alive')
else:
    print("the game closed")
    