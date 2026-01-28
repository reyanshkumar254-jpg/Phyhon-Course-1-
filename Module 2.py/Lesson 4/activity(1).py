string= input("please enter your own word-")

chrac= input("Please enter the chracter whose frequency has to be found-")

i= 0
count= 0

while(i < len (string)):

    if(string[i] == chrac):
        count= count + 1
    
    i= 1+i

print("The total number of times",chrac, "has occured= " , count)  