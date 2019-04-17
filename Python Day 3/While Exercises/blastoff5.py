import time

starting_number = int(input("starting number? "))
i = 0
while i < starting_number:
  print(starting_number - i)
  i = i + 1  
  time.sleep(1)
