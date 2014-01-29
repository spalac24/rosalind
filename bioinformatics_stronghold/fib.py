import collections
import sys

cin = open('rosalind_fib.txt','r')

n,k = map(int,cin.readline().split())


a = 0
p = 1
n -=1
while n > 0:
    a,p = a+p,a*k
    n -= 1
print (a+p)
cin.close()
