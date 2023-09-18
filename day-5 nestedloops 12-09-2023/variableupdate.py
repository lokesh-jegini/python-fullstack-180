row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

i = 1
j = 1
original_column = column

while i < row: 
    while column > j: 
        if column <= i:
            print("*", end="")
        else:
            print(" ", end="")
        column -= 1
    column = original_column  # Reset column to its initial value before moving to the next row
    print("")
    i += 1
