
def factorial(num):
    '''
    The function calcualtes the factorial of a number

    :param num: int -> this must be an integer
    :return: int -> factorial of num

    ex: 3! = 3 * 2 * 1
    '''
    assert num >=0, f'Can not handle negative number'
    if num in [0,1]:
        return 1
    if num > 0:
        out = num * factorial(num - 1)
        return out

def permutation(n, r):
    assert n >= r, f'r cannot be greater than n'
    out = factorial(n) / factorial(n - r)
    return out

def combination(n, r):
    assert n >= r, f'r cannot be greater than n'
    out = factorial(n) / (factorial(r) * factorial(n - r))
    return out