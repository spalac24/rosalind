import collections
import sys

cin = open('rosalind_revc.txt','r')

s = cin.readline().strip()
s = list(s)
s.reverse()


d = {'A':'T','T':'A','C':'G','G':'C'}

r = ""

for i in s:
    r += d[i]

print r
