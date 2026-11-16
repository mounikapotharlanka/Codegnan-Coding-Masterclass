
n = int(input("Enter N: "))

best_start = 1
best_terms = 1

for start in range(1, n + 1):
    num = start
    count = 1

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

        count += 1

    if count > best_terms:
        best_terms = count
        best_start = start

print("Start =", best_start)
print("Terms =", best_terms)
