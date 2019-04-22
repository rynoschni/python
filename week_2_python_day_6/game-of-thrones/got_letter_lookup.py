from characters import characters

list_of_characters = []
letter_input = input("Which letter would you like to look up? ")

# Characters whose names start with A
for character in characters:
    if character['name'][0] == letter_input:
        list_of_characters.append(character['name'])

number_of_characters_with_letter = len(list_of_characters)

print("There are %d characters whose names begin with %s" % (number_of_characters_with_letter, letter_input))