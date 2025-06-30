# Get input for number and checks this number has palindrome or not with an "if loop" and output the result.

number = input("Please enter the number : ")
if number == number[::-1]:
    print(f"{number} has a palindrome.")
else:
     print(f"{number} has not a palindrome.")