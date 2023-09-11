# python-fullstack-180
Here we are starting from the backend course then mongodb then we move to frontend technologies
Day-1 Bascis and setup of python
Day-2 Variables and arithmetic operators
      1)Program-1 by using arithmetic operator peform add,sub,mul,div,expo
      2)area of triangle = 1/2 * base * height
      3)#calculate age in days

Day-3
Day-4 Nested concept
      If
      For
      While
      Functions
      Array =[] 
      Object={}
      Each and every concept have structure --means syntax
      if the same syntax is wrappen with same syntax then it is nested type
-------
Why we are using nested when we are using nested
if the condiond is true then we enter inside the block (once we enter inside block we can print the statements directly ,if we want to check condition then if is true then we want to go for print then we use nested type)


--------------------------------------------
build program logics from day-1 with differnt concepts
how we are implement build block of code from day-1

1)hard code value with more statements (single input single output) (day -1 and day-2)
2) dyamic varibale value from the user during runtime (different input different output)(day-3)
3)when we run the program all statems ar are printing to avoid this we use conditional block concept (based on the condition certain blok of code is executed remain block of code is not execute)
4)when we run the program entire code is execute from start to bottom  to avoid this we go for the function concept
5)in realtime we did not use input method (so we go for funtion arugument concept in the realtime concept for getting output from the user)

----------------
loop:-let numbers = [1, 2, 3, 4, 5]; //for single variable more vales are assigned for printing eachand evety values individually we are using index values
here we are printing variable value continuosly 
//how we know the work want to repeately

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}

starting and ending point must and should for the loops

let i = 0; //initial
 i < numbers.length; final
 i++ increment of one one value

numbers[i]

----------------
the statements which are present inside loop will execute continuously untill the condition become fails
when we run the statements repeated 
if we want print same structure or logic on that time we wrap that staements inside loop

---------------
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    console.log(`${i} is even`);
  } else {
    console.log(`${i} is odd`);
  }
}

-----------------this is execute single time
if (i % 2 === 0) {
    console.log(`${i} is even`);
  } else {
    console.log(`${i} is odd`);
  }







