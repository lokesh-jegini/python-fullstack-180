x = 10  # Global variable
print(x)

def my_function():
    global x  # Use the global keyword to indicate that we're referring to the global variable 'x'
    x = 20    # Update the global 'x' to 20
    print(x)

my_function()  # Output: 20
print(x)  # Output: 20 (global 'x' has been updated to 20)
