person = input("What is your name? ")
subject = input("what is your favorite subject? ")

def make_madlib(person, subject):
    madlib = print ('your name is %s and your favorite subject is %s' % (person, subject))
    return madlib

make_madlib(person, subject)