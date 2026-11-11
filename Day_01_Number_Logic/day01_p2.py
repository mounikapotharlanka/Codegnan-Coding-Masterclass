num = int(input("Enter a number: "))
original = num
reverse = 0
if num < 0:
    print("Not Palindrome")
else:
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
