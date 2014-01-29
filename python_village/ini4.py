arr = raw_input().split()
ar = map(int,arr)
sum = 0
for i in range(ar[0],ar[1]+1):
    if i%2 == 1:
       sum = sum+i
print sum
