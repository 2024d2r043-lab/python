base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1
i = 1

while i <= exp:
    result *= base
    i += 1

print(f"{base} raised to the power {exp} is {result}")
