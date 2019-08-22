# # python-basics1-review-cw
#
# ### Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.
#
# userInput = input("Enter something. Enter 'q' to quit ")
# while userInput != 'q':
#     print(userInput)
#     userInput = input("Enter something. Enter 'q' to quit ")
# # ### Problem 2:
# # Ask the user for their name. Then ask the user for a number of times they want their name printed.
# # Print the number of times the user want their name printed. If they enter a negative or zero, tell them to ask again.
# #


# ### Problem 3:
# Create a program that takes user input in a while loop. If they enter 1, print 1. If they enter 2, print 2.
# If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.
#
# userInput = input("Enter 1 to print 1, Enter 2 to print 2, Enter 3 to print 3, Enter 'q' to quit ")
# while userInput != 'q':
#     if userInput == '1':
#         print("1")
#     elif userInput == '2':
#         print("2")
#     elif userInput == '3':
#         print("3")
#     else:
#         print("ERROR")
#     userInput = input("Enter 1 to print 1, Enter 2 to print 2, Enter 3 to print 3, Enter 'q' to quit")
# ### Problem 4:
# Create a program that takes the user input until they enter 'q'.
# You should store all of their input and separate the input with a comma.
# Once they enter 'q', print all of the comma separated words they entered.

storedInput = ""
userInput = input("Enter something. Enter 'q' to quit. ")
while userInput != 'q':
    storedInput = storedInput + " , " + userInput
    userInput = input("Enter something. Enter 'q' to quit. ")
print(storedInput)