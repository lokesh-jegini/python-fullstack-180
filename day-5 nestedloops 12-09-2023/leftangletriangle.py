#right angle trianlge by using the while
i=1
j=1
row=10
column=10

#if we are running loop we nedd starting and ending point (start is 1 and end is 10)

#to from step1 to step 10 (we are using increment operator) 
#increment and decrement operator are used of the looping purpose
# when we use incerement opertator (+) (we are print data from the left to right)
# when we use decrement opertator (-) (we are print data from the   right to left)
#if we use   i<row for cheking conditon single time
# if we use i<row start and end point comprasion on that time we give incepent operator base on the which block we are present (tat mean inner ot=r outer loop i or j)
while i<row: #for cheking condition we need two values (for enable true and fales)
    while column>j: # here are commin from the end point
       if column<=i:
            print("*", end="")
       else:
            print(" ", end="")
       column-=1 #here in block we are updatin the varibale
    column=column
    print("")
    i+=1

        
# if both row and column are go in the same direction on tattime we use increment 
#if both are in oposite the decrent
