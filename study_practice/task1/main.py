def check_lucky_ticket():
  amount = 0
  for a in range(10**n):
    a = list(str(a).zfill(n))
           
    a1 = [int(i) for i in a[:len(a)//2]]
    a2 = [int(i) for i in a[len(a)//2:]]
    if sum(a1) == sum(a2):
      amount += 1 
  print('The amount of lucky tickets', amount)

while True:
    try:
      n = int(input('Enter n: '))
      if n%2 != 0:
        print('Number must be odd!')
        continue
      break
    except:
        print('Your number from 2 to 100 must be odd!')

check_lucky_ticket()

