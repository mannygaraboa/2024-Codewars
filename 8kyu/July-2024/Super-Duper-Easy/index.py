# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    if a == str:
        print("Error")
        return 0
    else:
        print((a*50) + 6)
        return (a*50) + 6

problem(90)