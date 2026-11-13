L = int(input("Enter starting number: "))
R = int(input("Enter ending number: "))
found = False
for n in range(L, R + 1):
    if n > 1:
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        if count == 2:
            print(n, end=" ")
            found = True
if not found:
    print("None")
