number = int(input("Enter the number-"))
n = int(input("Enter how many powers you want-"))

print("Powers of", number, "are-")

result = 1

for i in range(1, n + 1):
    result = result * number
    print(number, "power", i, "=", result)
