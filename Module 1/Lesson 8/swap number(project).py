#Sir ka code

a= 24
b= 37
a= a+b
b= a-b
a=a-b
print(a, b)


#mera code
a = int(input("Enter first value-"))
b = int(input("Enter second value- "))
c = int(input("Enter third value- "))

print("\nBefore swapping:") 
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping the values
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)