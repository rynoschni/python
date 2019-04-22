from characters import characters

dead_characters = []

# Characters whose names start with A
for character in characters:
    if character['died'] != "":
        dead_characters.append(character['name'])

print("%d characters are dead" % len(dead_characters))