num = int(input("Enter a number: "))
original = num
temp = num
if num < 0:
    print("Not an Armstrong Number")
else:
    digits = 0
    if temp == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp = temp // 10
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10
    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
