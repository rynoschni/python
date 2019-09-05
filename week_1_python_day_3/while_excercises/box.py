# size = 5
width = int(input("width? "))
height = int(input("height? "))

# let's use 2 nested loops:
# - an outer loop that draws rows
# - an inner loop that draws columns

# Our "outer loop" determines how many rows to draw
# of our box.
y = 0
while y < height:

    # Our "inner loop" draws a row at a time
    x = 0
    while x < width:

        # We only want to draw the sides of the box.
        # We can test our x and y values to see
        # if are at the top, bottom, left, or right.

        # Here are some booleans that reflect
        # whether we are at an edge
        is_top    = (y == 0)
        is_bottom = (y == (height - 1))
        is_left   = (x == 0)
        is_right  = (x == (width - 1))

        # If we are at an edge, draw a star
        if is_top or is_bottom or is_left or is_right:
            print('x ', end='')
        # Otherwise, draw a space
        else:
            print('  ', end='')

        # Move our inner loop closer to the end    
        x = x + 1

    # When the inner loop is finished, that means it
    # drew a row. We print() to make it start a new line.
    print()


    # Move our outer loop closer to the end
    y = y + 1