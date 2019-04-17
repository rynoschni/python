
starting_number = int(input("starting number? "))
if starting_number <= 20:
  i = 0
  while i < starting_number:
    print(starting_number - i)
    i = i + 1  
else:
  print("sorry, too big!")
