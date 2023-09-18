#right angle trianlge by using the while
i=1
j=1
row=10
column=10

while i<=row:
    while j<=column:
        if i>=j:
          print("*",end=" ")
        j+=1 # here loop hold j value as 10 when it come out of the loop we made this j as 1 on that time only we can acheive the triangle 
    print(" ")
    j=1
    i+=1
    
