
go = True
while go:
  factors = []
  number = int(input("Enter a number to factor: "))
  if number < 100000:
    i = 1
    while i < number:
      if (number % i == 0):
        print("%d " % (i), end='')
      i = i + 1
    print()
  else:
    print("Too big.")
  answer = input("another (Y/N)? ")
  if answer.upper() != "Y":
    go = False
print("k. thanks. bye!")
