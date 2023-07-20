#program to print ASCII values of a character

a=input("Enter a character: ")

if len(a) == 1:
    ascii_value = ord(a)
    print(f"The ASCII value of '{a}' is: {ascii_value}")
else:
    print("enter a single character")

