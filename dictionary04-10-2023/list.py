times=int(input("enter list append times"))
i=0
listappend=[]
while i < times :
    dicdata={"name":"","age":"","email":""}

    name = input("Enter name: ")
    age=input("Enter age:")
    email=input("Enter gamil")
    # dicdata["age"] = input("Enter age: ")
    # dicdata["email"] = input("Enter gamil: ")
    dicdata.update({"name":name,"age":age,"email":email})
    
    listappend.append(dicdata)
    i=i+1

print(*listappend,sep="\n") 

#print({'name': 'loki', 'age': '1', 'email': 'gmail'}, {'name': 'loki1', 'age': '2', 'email': 'gmail2'},sep="\n")
 
 

