# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

# Enter 7, 2, bob, 10, and 4 and match the output below.
# Expected output:
# Invalid input
# Maximum is 10
# Minimum is 2

#### first approach functions
inp = input("Enter a number or 'done': ")
entries = []

while inp != "done":

    # try/except to validate input
    try:
        entry = int(inp)
    except:
        print("Invalid input")

    # store inputted numbers
    entries.append(entry)
    inp = input("Enter a number or 'done': ")

print("Maximum is", max(entries))
print("Minimum is", min(entries))


#### another approach using functions
# def getMin(arr, smallest):
#     for i in arr:
#         if smallest is None:
#             smallest = i
#         elif smallest > i:
#             smallest = i
#
#     return smallest
#
#
# def getMax(arr, largest):
#     for i in arr:
#         if largest is None:
#             largest = i
#         elif largest < i:
#             largest = i
#
#     return largest
#
#
# largest = None
# smallest = None
#
# nums = []
#
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     else:
#         try:
#             entry = int(num)
#         except:
#             print("Invalid input")
#     nums.append(entry)
#
# print("Maximum", getMax(nums, largest))
# print("Minimum", getMin(nums, smallest))
