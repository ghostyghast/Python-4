def square(x: int | float) -> int | float:
    '''
    square(x: int | float) -> int | float:
    squares the given number and returns the result
    '''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''
    pow(x: int | float) -> int | float
    return the given number to the power of itself
    '''
    return x ** x


def outer(x: int | float, function) -> object:
    '''
    outer(x: int | float, function) -> object:
    Returns inner function, and initializes count
    to zero
    '''
    count = 0

    def inner() -> float | int:
        '''
        inner() -> float | int:
        Nested function that applies given function
        to x, and returns the result
        Every call, the function will remember the result
        stored in nonlocal varbiabe and re-apply function
        '''
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count
    return inner
