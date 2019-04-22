
# Prompt user over and over and over again until they say "bye"
# but if they say "bye" three times
# just exit the program

# Initial condition is set to "True"
bye_count = 0

# Initial condition is equivalent to True
while bye_count < 3:
    # Initial condition is set to True
    should_run = True

    # Use the that condition as part of the `while`
    while should_run:
        user_input = input("What? ")
        print("%s" % (user_input,))

        # Eventually, set the condition to False
        if user_input == "bye":
            should_run = False

            # Reassigning bye_count using its previous value
            bye_count = bye_count + 1
        print(bye_count)

