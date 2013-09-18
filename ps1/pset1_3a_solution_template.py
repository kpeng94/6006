# This solution template should be turned in through our submission site, at
# https://alg.csail.mit.edu

######################################################################################
### WARNING:                                                                       ###
### Be sure to write the Python code yourself!  We do run sophisticated automated  ###
### comparisons between each pair of programs turned in.  We are saddened and      ###
### troubled each year when a few studentsturn in nearly identical programs, and   ###
### we have to administer appropriate consequences.  It is better to turn in a     ###
### statement that you didn't have time to complete the assignment than to turn in ###
### the same code as someone else.                                                 ###
######################################################################################

######################
### Problem 1-3(a) ###
######################

# Recommended to use with "pypy" implementation of python, for speed, but not necessary.

import math # to get math.factorial
import time # to get time.time

#
# Iterative Implementation of Factorial
#
def fact1(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

#
# Library Implementation of Factorial
#
def fact2(n):
    return math.factorial(n)

#
# Divide and Conquer Implementation of Factorial
#
def fact3(n):
    return fact3Helper(1, n)

def fact3Helper(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) / 2
        return fact3Helper(start, mid) * fact3Helper(mid + 1, end)
