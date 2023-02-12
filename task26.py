def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n-1)

a = factorial(6)
print(a)


factorial = {6, 5, 4, 3, 2, 1}

total = 1
for num in factorial:
    total *= num

print(total)