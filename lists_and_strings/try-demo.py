# prompt the user until they give a valid number as input
# 1. initial condition
is_not_valid = True

# 2. while loop using the condition
while is_not_valid:
    # get some input from the user
    user_input = input("gimme a number ")
    try:
        # try to convert it to an integer
        user_int = int(user_input)
        # 3. set the condition so that our while loop ends
        is_not_valid = False

        # then print it out
        print("You gave me the number %d" % (user_int,))
    except:
        print("BZZZZZTTT! %s IS NOT A NUMBER!!!!" % user_input)
        pass # this does nothing, except hold the spot for an indented body