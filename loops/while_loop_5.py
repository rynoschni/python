title = "The Green Lantern Corp"

count = 0

while count < len(title):
    if (count % 2) == 0 and title[count] != ' ':
        print(title[count])
    count += 1
