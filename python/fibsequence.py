# fibsequence.py
# Write a program that outputs the nth Fibonacci number, 
# where n is a user-entered number. So if the user enters 4, 
# the program should output 3 (without outputting the intermediate steps). 
# Use a recursive function compute_nth_fib that takes n as a parameter
# and returns the Fibonacci number. The function has two base cases: 
# input 0 returns 0, and input 1 returns 1.

def compute_nth_fib_helper_method(fib_counter_helper):
    return fib_counter_helper + 1

def compute_nth_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + compute_nth_fib(num - 1)
    
passes = int(input('Enter number of passes: '))
print(compute_nth_fib(passes))