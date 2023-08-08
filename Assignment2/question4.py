"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


def ans(s):
    li = []
    for i in s:
        li.append(i)
        print(li)
    # print(s.split())
    print(tuple(s))


s = list(input().split())
ans(s)
# print(s)
# print(tuple(s))
