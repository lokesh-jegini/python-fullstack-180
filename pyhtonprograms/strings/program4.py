#print a string in reverse order by taking characters from the user

data=input("enter some data")
lengthvalue=len(data)-1  #length always start from one but index start from o but we are acess thought the index so we remove one value
i=0
while(lengthvalue>=i):
    print(data[lengthvalue])
    lengthvalue-=1
