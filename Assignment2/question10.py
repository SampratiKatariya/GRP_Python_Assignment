"""
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

"""


def solution(l):
    ans = set(l)
    ans = list(ans)
    val = sorted(ans)
    for i in val:
        print(i, end=" ")


l = list(input().split())
# print(l)
# ans = set(l)
# print(ans)
# ans = list(ans)
# print(ans)
# val = sorted(ans)
# print(val)
solution(l)
