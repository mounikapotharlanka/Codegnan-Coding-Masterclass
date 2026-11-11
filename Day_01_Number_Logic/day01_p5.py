num = int(input("Enter a number: "))
candidate = max(2, num + 1)
while True:
    is_prime = True
    divisor = 2
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print("Next prime number:", candidate)
        break
    candidate += 1
