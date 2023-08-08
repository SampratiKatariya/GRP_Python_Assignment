"""
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

li = []
while True:
    s = input()
    if s:
        li.append(s.upper())
    else:
        break
for i in li:
    print(i)
