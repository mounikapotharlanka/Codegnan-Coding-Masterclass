n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")
