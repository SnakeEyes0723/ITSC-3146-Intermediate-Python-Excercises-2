# For this part of the assignment, I had to learn how to call random numbers, which I learned how to do with the randint() function from here: https://www.geeksforgeeks.org/python-randint-function/

import random
import time


def fib(number: int):
    numberlist = [] * number
    numberlist.append(0)
    numberlist.append(1)
    i = 2
    while(i < number):
        sum = numberlist[i-1] + numberlist[i-2]
        numberlist.append(sum)
        i = i + 1
    return numberlist[number - 1]

n = random.randint(15, 35)
print("fib(" + str(n) + ") = " + str(fib(n)))
print("fib(" + str(n) + ") took " + str(time.time()) + " seconds")