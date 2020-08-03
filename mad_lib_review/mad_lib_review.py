madlib_word_choices = {
    "noun": "",
    "verb": "",
    "adjective": ""
}

madlib_word_choices["noun"] = input("Enter a noun: ")
madlib_word_choices["verb"] = input("Enter a verb: ")
madlib_word_choices["adjective"] = input("Enter an adjective: ")

print("The %s %s is %s" % (madlib_word_choices['adjective'], madlib_word_choices['noun'], madlib_word_choices['verb']))
