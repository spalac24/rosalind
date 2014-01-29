import sys

lines = open('rosalind_ini5.txt','r').readlines()


s = ""
for idx,l in enumerate(lines):
    if (idx%2 == 1):
        s = s+l
    
open('rosalind_ini5.out','w').write(s)
print s
