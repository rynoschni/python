# Effectively, we're iterating over TWO items:
# 1 - A sequence (in this case, a list)
# 2 - A string, from a user input

# Our String
text = "hello world"
# text = input("Please enter a phrase: ")

# Our comparison sequence
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']

# Our translation sequence
numbers = [4,   3,   6,   1,   0,   5,   7]

# Let's create a string to store our translation...
translation = ""

# Let's convert everything to uppercase
uppercased_text = text.upper()

# Loop through out text
index = 0
while index < len(uppercased_text):
    # Grab the letter from our text
    letter = uppercased_text[index]

    index = index + 1
    # print("the letter is ", letter)
    # print("the index is ", letters_to_convert.index(letter)

    # Create a placeholder for our converted letter
    letter_to_add_to_translation = ""

    # Loop through our letters_to_convert list, comparing our letter from above
    index_inner_loop = 0
    while index_inner_loop < len(letters_to_convert):
        letter_to_convert = letters_to_convert[index_inner_loop]
        # print("looking at ", letter_to_convert)

        # Do we have a match??
        if letter == letter_to_convert:
            # WE DO HAVE A MATCH!!!
            # print("\n********** found it! %s \n\n" % letter)
            # print("want to replace with %s" % numbers[counter])
            # translation = translation + str(numbers[counter])

            letter_to_add_to_translation = str(numbers[index_inner_loop])
            break
            # dear self, break out of loop after finding good replacement
            # otherwise, you overwrite with the original letter
        else:
            # NO MATCH :(
            # print("just use", letter)
            # translation = translation + letter
            letter_to_add_to_translation = letter

        # Keep on loopin'...
        index_inner_loop = index_inner_loop + 1

    # We need to update our translation with either
    # a converted letter, or the original letter...
    translation = translation + letter_to_add_to_translation

# Print that translation
print(translation)
