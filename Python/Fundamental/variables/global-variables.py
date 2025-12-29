# Global variables
# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()

print("Python is " + x)



