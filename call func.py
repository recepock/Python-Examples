from myMath import factorial, add, multiply, evaluate
from math import sqrt

print(factorial(34))
print(sqrt(16))

print(add(6,9))
print(multiply(5,2))
print(evaluate(add,34, 66))
print(evaluate(multiply,34, 66))

function_name = input(' enter your function name')

print(evaluate(function_name,2,5))
