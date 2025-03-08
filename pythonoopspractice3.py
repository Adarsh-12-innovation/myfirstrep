
def decorator_msg(func):
    def comment():
        print ('this is first time writing abstract code')
        func()
    return comment()

    

@decorator_msg
def message():
    return print('i have executed the decorator function')


