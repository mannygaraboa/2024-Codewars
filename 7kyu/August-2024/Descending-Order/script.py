# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    list1 = str(num)
    list2 = [*list1]
    list2.sort(reverse=True)

    x = int(''.join(map(str, list2)))

    print(list2)
    print(x)

    return x

descending_order(493)

# Best Practice:

    # def Descending_Order(num):
    #     return int("".join(sorted(str(num), reverse=True)))