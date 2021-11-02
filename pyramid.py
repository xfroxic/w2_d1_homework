# Frank Goshko 11/1/21
# Pyramid assingment
# Create a pyramid of X's for n number of levels.

# .....X.
# ....X.X.
# ...X.X.X.
# ..X.X.X.X.
# .X.X.X.X.X.


print("Let's make a pyramid of X's")
    
n = input("How many levels should there be?")
x = int(n)

def pyramid(x):
    # number of .'s needed
    a = x - 1
    # number of rows
    for b in range(0, x):
        # print a . at the end of each row
        for c in range(0, x):
            print(end=".")            
        # make sure x goes down by 1 each loop
        x = x - 1
        # set number of columns, print X's, and end each row
        for b in range(0, b+1):
            print("X.", end="")
        print("\r")

pyramid(x)
