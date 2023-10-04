#by using for
data=input("enter a string for fining length")
count=0
def stringdata(data):
    global count
    for i in data: #when we use "in" key word in the loops we should not use increment it wok like index base
      count=count+1
    return count
result=stringdata(data)
print(result)

#by using while
data1=input("enter a string for fining length by using the while method")
def secondmethod(data1):
   value=0
   while data1[value:]:
      value=value+1
   return value
finalresult=secondmethod(data1)
print(finalresult)


   
      


