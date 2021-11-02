# Frank Goshko 11/1/21
# Calculator assingment
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... 
#   Loop until the user chooses not to perform any more calculations.

# I read it's good practice to name your program "main"
def main():

    print("A simple Python calculator. Please enter two numbers:")

    num_1 = input("First number?") 
    num_2 = input("Second number?")
    operand = input("Please enter one of the following operation types: + - * / ")
    x = int(num_1)
    y = int(num_2)

    def calculation(x, y, operand):
        if operand == "+":
            result = x + y
            return (result)

        elif operand == "-":
            result = x - y
            return (result)

        elif operand == "*":
            result = x * y
            return (result)

        elif operand == "/":
            result = x / y
            return (result)

        else:
            return ("Invalid operand type")

    print (calculation(x, y, operand))

# Using a while loop to run the program until the user decides to quit
while True:
    main()
    if input("Do you have more calculations to do? ('y' for yes or 'n' for no)") == "n":
        print ("You are the weakest link. Goodbye.")
        break

    
