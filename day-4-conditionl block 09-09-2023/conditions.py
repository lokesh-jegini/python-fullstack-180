#if
#if else
#if elif
#if elif else
#from here on ward block concept will start
#when i run the program code is executed from the top to bottom on that time all block are executed to over come this they introduced functions concept
#we can call particular function which thing we need eg vote check or even number checking
#program-1 write a program to check wether the person is elgible for vote or not
age=input("enter your age")
age=int(age)
if(age>18):
    print("yor are elgible for vote")
else:
    print("you are not elgible for vote")

#program-2 To check the given number is even or odd
number=input("enter a number")
number=int(number)
if(number%2==0):
    # print("Entered number "+number+,"is even") //how to do object literal concept
     print("Entered number is even")
else:
    print("entered number is odd number")

#program-3 Check the given number is divisible by 7 or not

#based on the condition some statements want to execute on the time  we given that statements inside block (id concept consit block so we are using if concept)

seveennumber=input("enter a number to check divisible by seveen or not")
seveennumber=int(seveennumber)
if(seveennumber%7==0):
    print("Given number is divisible by seveen")
else:
    print("Given number is not divisble by seveen")

#program 4 write a program to calculate the electricity bill by accept the uints from the user
electricunits=input("enter electricity uints")
electricunits=int(electricunits)
if(electricunits != ""):
    if(electricunits>100):
       afterremove= electricunits-100
       if(afterremove>=100):
           secondtarif=afterremove-100
           secondtarifrate=100*5
           if(secondtarif):
               finalresult=secondtarif*10+secondtarifrate
               print(finalresult)
else:
    print("enter valid units")