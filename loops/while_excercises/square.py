# size = 5
# width = int(input("width? "))
#height = int(input("height? "))
width = 10
height = 10

# let's use 2 nested loops:
# - an outer loop that draws rows
# - an inner loop that draws columns

# Our "outer loop" determines how many rows to draw
# of our square.
y = 0
while y < height:

    # Our "inner loop" draws a row at a time
    x = 0
    while x < width:

        # Draw!
        print('*', end='')

        # Move our inner loop closer to the end
        x += 1

    # When the inner loop is finished, that means it
    # drew a row. We print() to make it start a new line.
    print()


    # Move our outer loop closer to the end
    y = y + 1