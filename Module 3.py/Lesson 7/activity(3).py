def add (P,Q):
    return P + Q
def minus(P,Q):
    return P - Q
def into(P,Q):
    return P * Q
def by(P,Q):
    return P / Q

print("Please select the operation you want to conduct")
print("a- add")
print("b- minus")
print("c- into")
print("d- by")

chocie= input("please enter your chocie")

num_1=int(input("Please enter the 1st number"))
num_2=int(input("please enter the 2nd number"))

if chocie == "a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif chocie == "b":
    print(num_1,"-",num_2,"=",minus(num_1,num_2))
elif chocie == "c":
    print(num_1,"*",num_2,"=",into(num_1,num_2))
elif chocie == "d":
    print(num_1,"/",num_2,"=",by(num_1,num_2))
else:
    print("This input is invalid")