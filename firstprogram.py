a=5
b=10
sum=a+b
print("The sum of",a,"and",b,"is",sum)
num = input("Enter a number to check if it is a palindrome: ")
if num == num[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")