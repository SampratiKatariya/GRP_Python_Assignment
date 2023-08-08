"""
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""


def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n > 0:
        rem = n % 10
        n = n // 10
        decimal += rem * power
        power = power * 2

    return decimal


l = list(input().split(','))
li = []
for i in l:
    li.append(binaryTodecimal(int(i)))
bi = []
for i in li:
    if i % 5 == 0:
        bi.append(bin(i)[2:])

# print(li)
for i in bi:
    print(int(i))
# print(bi)
