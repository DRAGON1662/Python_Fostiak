def pos_l(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return pos_l(n-1) + pos_l(n-2)

a = 10
lst = []
for i in range(a):
    lst.append(pos_l(i))
print(lst)