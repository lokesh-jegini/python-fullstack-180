#take a input from the user and print each and evey character by using while loop for the positive index
#index start from zero but length start from 1
data=input("enter a string")
endvalue=len(data)

i=0
while(i<endvalue-1): #we nedd to give endvalue or end-1
 print(data[i])
 i+=1
print(endvalue)
# lokesh