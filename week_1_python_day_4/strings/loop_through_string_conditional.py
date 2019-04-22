title = "Green Lantern Corp"
STOP = 10
counter = 0
while counter < STOP:
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter = counter + 1
