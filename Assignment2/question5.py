"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also, please include simple test function to test the class methods.

"""


class input_output:

    def __init__(self) -> None:
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())


obj = input_output()
obj.getString()
obj.printString()

