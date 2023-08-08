"""
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
li = []
bi = []
for i in range(1000, 3001):
    li.append(i)


def even_calculator(num):
    abc = num
    flag = True
    while num > 0:
        num, digit = divmod(num, 10)
        if digit % 2 != 0:
            flag = False
    if flag:
        bi.append(abc)


for i in li:
    even_calculator(i)

print(bi)
