row=int(input("enter a row number"))
column=int(input("enter a column number"))
i=1
j=1
original=column

while i<row:
    while column > j:
        if column <= i:
            print("*",end="")
        else:
            print(" ",end="")
        column-=1
    column=original
    print(" ")
    i+=1