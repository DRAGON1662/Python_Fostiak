amount = int(input("How many numbers? "))

def common_luca_numbers(): 
  n1, n2 = 2, 1
  count = 0
  if amount <= 0:
    print("Enter a positive integer")
  elif amount == 1:
    print("First Luka number -", n1)
  else:
    print("Luka sequence:")
    while count < amount:
        if n1 != 1 and all(n1%i!=0 for i in range(2,n1)):
          print(n1)
        nth = n1 + n2
      # update values
        n1 = n2
        n2 = nth
        count += 1

common_luca_numbers()