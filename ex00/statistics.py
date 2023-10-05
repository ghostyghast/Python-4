def mean(nums, n_len):
    """mean(list of numbers, length of list)
    calculate and return mean of given list"""
    return sum(nums) / n_len


def median(nums, n_len):
    """mean(list of numbers, length of list)
    calculate and return median of given list"""
    if n_len % 2 == 0:
        median = mean([nums[n_len // 2 - 1], nums[n_len // 2]], 2)
    else:
        median = nums[n_len // 2]
    return median


def quartile(nums, n_len):
    """quartile(list of numbers, length of list) -> array of 2
    calculate then return the quartiles (only 25% and 75%) of given list"""
    lower = nums[:n_len // 2 + 1]
    upper = nums[n_len // 2:]
    return [float(median(lower, len(lower))), float(median(upper, len(upper)))]


def var(nums, n_len):
    """var(list of numbers, length)
    calculate the variance of given list and return it"""
    return sum(pow(x-mean(nums, n_len), 2) for x in nums) / n_len


def ft_statistics(*args, **kwargs) -> None:
    """ft_statistics(individual numbers, statistics wanted)
    function that takes a bunch of numbers then displays different
    statistics about the list of numbers"""
    assert all([isinstance(x, (int, float)) for x in args]), \
        "args must all be numbers"
    a_len = len(args)
    args = list(args)
    args.sort()
    for x in kwargs:
        if a_len < 4:
            print('ERROR')
        elif kwargs[x] == 'mean':
            print('mean :', mean(args, a_len))
        elif kwargs[x] == 'median':
            print('median :', median(args, a_len))
        elif kwargs[x] == 'quartile':
            print('quartile :', quartile(args, a_len))
        elif kwargs[x] == 'var':
            print('var :', var(args, a_len))
        elif kwargs[x] == 'std':
            print('std :', var(args, a_len) ** 0.5)
