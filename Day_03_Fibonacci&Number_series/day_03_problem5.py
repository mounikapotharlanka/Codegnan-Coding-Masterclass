arr = list(map(int, input("Enter numbers: ").split()))

n = len(arr)

d = (arr[-1] - arr[0]) // n

for i in range(n - 1):
    if arr[i + 1] - arr[i] != d:
        print(arr[i] + d)
        break