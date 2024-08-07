# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    if isinstance(a, str):
        print(a, ": Error")
        return "Error"
    else:
        total = (a*50) + 6;
        print("Total:", total)
        return total

problem("Hello")

# Best Practice:
# def problem(a):
#     try:
#         return a * 50 + 6
#     except TypeError:
#         return "Error"