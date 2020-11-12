def number_of_bottles():
    for i in reversed(range(99)):
        if i > 1:
            print(i)
            print(' bottles of milk. ')
            print(i)
            print(' bottles of milk. Take one down and pass it around')
            print(i-1)
            print('bottles of milk on the wall.')
        elif i == 1:
            print(i)
            print('bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.')
            print('No more bottles of milk on the wall, no more bottles of milk.')
            print('Go to the store and buy some more, 99 bottles of milk on the wall.')
        
number_of_bottles()