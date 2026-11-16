
n = int(input("Enter a number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n and n > 1:
    print("Perfect number")
else:
    print("Not perfect")
