import madlib_generator # now using the "madlib_generator" module

want_to_write_a_madlib = 'yes'

while (want_to_write_a_madlib == 'yes'):
    user_name = input('what is your name? ')
    user_subject = input('what is your favorite subject? ')

    print(madlib_generator.make_madlib(user_name, user_subject))

    want_to_write_a_madlib = input('Would you like to play again? ')