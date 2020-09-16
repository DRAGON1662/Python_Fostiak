n = int(input('Enter n: '))
if n%2 == 0 and n <= 100 and n >= 0:
  amount = 0
  for a in range(10**(n-1), 10**n):
      a = list(str(a))
      a1 = [int(i) for i in a[:len(a)//2]]
      a2 = [int(i) for i in a[len(a)//2:]]

      if sum(a1) == sum(a2):
          amount += 1 
  print('The amount of lucky tickets ', amount)
else:
  print('Your number from 2 to 100 must be odd!')