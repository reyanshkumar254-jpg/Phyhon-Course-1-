temperature = int(input("What is the Temperature: "))

if temperature > 25:
    print("It is okay to wear light clothes.")
elif temperature >= 15:
    print("The weather is moderate.")
    print("You can wear normal clothes.")
else:
    print("It is cold.")
    print("It is not recommended to wear light clothes.")
