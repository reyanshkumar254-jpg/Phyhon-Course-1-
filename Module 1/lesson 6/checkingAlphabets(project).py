#First we have to find the Ascii value of a, z, A & Z
Chracter1="a"
Chracter2="z"
Chracter3="A"
Chracter4="Z"
#1 
Asciivalue1= ord(Chracter1)
print(Asciivalue1)
#2
Asciivalue2= ord(Chracter2)
print(Asciivalue2)
#3
Asciivalue3= ord(Chracter3)
print(Asciivalue3)
#4
Asciivalue4= ord(Chracter4)
print(Asciivalue4)

#Now the real code beginsthe rest was the warm up

alpha1=(input("Enter any character of your choice"))

if alpha1 >= 97 and alpha1 <= 122:
    print("The input is a alphabet, and to be more precise it is a Lower case alphabet")
elif alpha1 >= 65 and alpha1 <= 90:
    print("The input is a alphabet, and to be more precise it is a Upper case alphabet")
else :
    print("it is not a alphabet")