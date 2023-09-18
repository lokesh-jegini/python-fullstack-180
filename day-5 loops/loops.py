
#add the string numbers
number = int(input("Enter a number: "))
temp = 0
while number > 0:
    result = number % 10 
    temp += result 
    number = number // 10
print(temp)
number = 2
end = 10
i = 1
if number > 0:
    while i <= end:
        print(f"{number}*{i}={number * i}")
        i += 1  # Use 'i += 1' to increment i
else:
    print("Enter a valid number")