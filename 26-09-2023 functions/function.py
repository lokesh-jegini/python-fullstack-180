def sum():
    a=10
    b=20
    add=a+b
    print(add)

#take a input srom the users then add the numbers that all are odd numbers
# here i nedd sequen 10
def odd():
    number=int(input("enter a number"))
    result=0
    while number>0:
        if number%2 !=0 :
            number
            result+=number
            print(number)
        number-=1
    print(result)

    
#ascendiing order
def revers1():
    numbers=[10,200,6,70,80,100,9]
    i=0
    while j < len(numbers):
        if(numbers[i]>numbers[i+1]):
            numbers[i],numbers[i+1]=numbers[i+1],  numbers[i]
        j+=1    
        print(numbers)
    print(numbers)


def revers():
    numbers=[10,200,6,70,80,100,9]
    print(numbers)
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-1):
           if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(numbers)
revers()
