def common_luca_numbers(): 
  n1, n2 = 2, 1
  count = 0
  if amount <= 0:
    print("Enter a positive integer")
  elif amount == 1:
    print("First Luka number -", n1)
  else:
    print("Prime Luka sequence:")
    while count < amount:
        if n1 != 1 and all( n1%i!=0 for i in range(2,n1)):
          print(n1)
        nth = n1 + n2
      # update values
        n1 = n2
        n2 = nth
        count += 1

while True:
    try:
      amount = int(input("How many numbers? "))
      if amount <= 0:
        print("Enter a positive integer")
        continue
      break
    except:
        print('It must be an amount of numbers from 1')

common_luca_numbers()
