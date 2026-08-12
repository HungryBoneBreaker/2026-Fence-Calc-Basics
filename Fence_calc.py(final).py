# Check if the user types in a number greater than zero otherwise reset
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the human for a number
            response = float(input(question))

            # check that the number is more than 0
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
# Main routine starts here...

keep_going = ""
while keep_going == "":
    # Ask the user for both width and length and $ per meter of fence
    width = num_check("Width:")
    Length = num_check("Length:")
    cost = num_check("cost per meter:$")

    # calculate perimeter and cost ($) per meter
    perimeter = 2 * (width + Length)
    cost = perimeter * cost

    # Display output
    print(f" your area will be...{perimeter} units")
    print(f"The cost of your fencing will be {cost}:.2f")

    # Ask if the user wanted to keep going or not
    print()
    keep_going = input("press 'Enter' key tp keep going or any other key to quit")
    print()

print("Thank you for using my amazing Fencing cost per meter Calculator :)")
