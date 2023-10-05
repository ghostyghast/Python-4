def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count == limit:
                print('Error:', function, 'call too many times')
            else:
                count += 1
                function(*args, *kwds)
        return limit_function
    return callLimiter
