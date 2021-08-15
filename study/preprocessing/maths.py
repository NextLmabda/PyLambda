
class Maths:
    '''

    '''
    def __init__(self, n, r, decision):
        '''

        :param n:
        :param r:
        :param decision:
        '''
        print('I am running the init method')
        self.n = n
        self.r = r
        self.dec = decision

    def permutation(self):
        '''

        :return:
        '''
        assert self.n >= self.r, f'r cannot be greater than n' # unittesting
        out = self.factorial(self.n) / self.factorial(self.n - self.r)
        return out

    def combination(self):
        assert self.n >= self.r, f'r cannot be greater than n'
        out = self.factorial(self.n) / (self.factorial(self.r) * self.factorial(self.n - self.r))
        return out

    def factorial(self, num):
        '''
        The function calcualtes the factorial of a number

        :param num: int -> this must be an integer
        :return: int -> factorial of num

        ex: 3! = 3 * 2 * 1
        '''
        assert num >= 0, f'Can not handle negative number'
        if num in [0, 1]:
            return 1
        if num > 0:
            out = num * self.factorial(num - 1)
            return out

    def Decision(self):
        if self.dec == 'P':
            return self.permutation()
        else:
            return self.combination()


n, r = input('Please, enter two integers separated by space: ').split()
#n = int(input('Please, enter first integers: '))
#r = int(input('Please, enter second integers: '))

decision = input('What action do you want to perform, Enter P for Permutation and C for combination: ')

math = Maths(n=int(n), r=int(r), decision=decision)

result = math.Decision()

print(result)