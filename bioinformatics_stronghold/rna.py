import collections

s = list(raw_input())
cout = open('rosalind_rna.out','w')

for idx,v in enumerate(s):
    if v == 'T':
        s[idx] = 'U'

s = "".join(s)
print >> cout,str(s)
print s


cout.close()
