"""
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""


def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


n = int(input())
print(factorial(n))
