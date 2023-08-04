#Prime number
def isPrime(num):
    x=2
    while(x<=(num/2)):
        if(num%x==0):
            return False
        x+=1
    
    return True

lst=[]
for i in range(2,51):
    if(isPrime(i)):
        lst.append(i)

print("Prime numbers between 1 to 50 ",lst)


#Print table
def print_table(number):
    for i in range(1, 11):
        result = number * i
        print(number," * ",i," = ",(result))
        
print_table(3)

#Pallindrome
def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Reverse String
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)




