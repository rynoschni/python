
# Simplified version of the 
# while-loop-demo2.py program.
# You don't *actually* need to
# use nested loops ;)

# Prompt user over and over and over again until they say "bye"
# but if they say "bye" three times
# just exit the program

# Initial condition is set to "True"
bye_count = 0

# Initial condition is equivalent to True
while bye_count < 3:
    # Initial condition is set to True
    user_input = input("What? ")
    print("%s" % (user_input,))

    # Eventually, set the condition to False
    if user_input == "bye":
        # Reassigning bye_count using its previous value
        bye_count = bye_count + 1
    print(bye_count)

