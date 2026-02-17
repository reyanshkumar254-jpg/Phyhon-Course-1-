a= 23
b= 73
c=26
d=25
e=10
sum= a + b + c + d + e
print(sum)
average=sum/5
print(average)

Amount= int(input("How much you want to withdraw"))

note_1= Amount // 100
note_2= (Amount % 100) // 50
note_3= ((Amount % 100) % 50 ) // 10 

print(note_1)
print(note_2)
print(note_3)

print("Enter your amrks of 4 subjects:maths,science,english and hindi")
maths=int(input("maths"))
science=int(input("science"))
english=int(input("english"))
hindi=int(input("hindi"))

sum= hindi + maths + science + english
print(sum)
precentage=(sum/400)*100 
print(precentage)