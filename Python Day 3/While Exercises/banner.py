text = input('Text? ')
stars = ''

# The width of the top and bottom rows of the banner
# is the length of the text + 2 stars + 2 spaces
counter = 0
while counter < (len(text) + 4) :
  stars = stars + '*'
  counter = counter + 1

print(stars)
print("* %s *" % text)
print(stars)