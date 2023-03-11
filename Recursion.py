def compute_power(x, y):

    # Iterative Algorithm
    '''answer = 1
    for i in range(0, y):
        answer *= x

    return answer'''

    # Recursive Version
    if (y == 0):
        return 1
    else:
        return x * compute_power(x, y-1)


def factorial(x):
    if (x == 0):
        return 1
    else:
        return x * factorial(x-1)

    
def fib(x):
    if (x == 1):
        return 0
    if (x == 2):
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
        

x = 2
y = 10
print("{}^{} = {}".format(x, y, compute_power(x,y)))

x = 10
print("{}! = {}".format(x, factorial(x)))

print("fib({}) = {}".format(x, fib(x)))


                          
