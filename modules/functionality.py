def add(*numbers):
    sum = 0
    for number in numbers:
        sum+=number
    return sum


def mulitification(*a):
    '''
    this is just a function that takes multiple arguments 
    and return the result
    '''
    multi = 1
    for i in a:
        multi*=i
    return multi


def specific_function():
    print("hello world")

if __name__ == '__main__':
    print("calling the file directly")
    specific_function()
else:
    print("CALLING BY IMPORT")
