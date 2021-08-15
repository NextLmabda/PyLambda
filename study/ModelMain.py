from preprocessing.calculus import *

x = combination(10, 10)

y = (lambda x: x ** 2)(10)

z = (lambda x, y: x * y)(2, 3)

func = lambda x, y: x * y if (x > y) else x ** 3
print(x)

print(y)

print(z)

print(func(10, 12))

print((lambda x, y, z: x * y * z)(3, 4, 5))