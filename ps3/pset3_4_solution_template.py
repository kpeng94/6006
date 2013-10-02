# This solution template should be turned in through our submission site, at
# https://alg.csail.mit.edu

######################################################################################
### WARNING:                                                                       ###
### Be sure to write the Python code yourself!  We do run sophisticated automated  ###
### comparisons between each pair of programs turned in.  We are saddened and      ###
### troubled each year when a few students turn in nearly identical programs, and  ###
### we have to administer appropriate consequences.  It is better to turn in a     ###
### statement that you didn't have time to complete the assignment than to turn in ###
### the same code as someone else.                                                 ###
######################################################################################

###################
### Problem 3-4 ###
###################

# NOTE: For naive_multiply and karatsuba_multiply, you may
# only use the Python "*" operator on single digit multiplications
# and on multiplying numbers by powers of 10. You may also use the 
# Python "**" operator.
# 
# In those two functions, all uses for "*" should be of the form 
# a * b (where a and b are single digit numbers)
# or 
# a * (10**b) (a and b don't need to be single digit numbers)

#===================
# Problem 3-4a
#===================
# This function naive_multiply takes in two integers (or longs)
# and multiplies them together using the Grade School
# Multiplication Algorithm.
#
# Remember to only use the Python "*" operator in the manner described above.

def naive_multiply(x, y):


#===================
# Problem 3-4c
#===================
# This function karatsuba_multiply takes in two integers (or longs)
# and multiplies them together using the Karatsuba
# Multiplication Algorithm.
#
# Remember to only use the Python "*" operator in the manner described above.

def karatsuba_multiply(x, y):

import time
#===================
# Problem 3-4d
#===================
# You may want to use this function to time the runtimes of 
# naive_multiply, karatsuba_multiply, and the native
# python multiply. The time module might be useful to you.

def time_functions():

