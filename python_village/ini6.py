import collections

cin = open('rosalind_ini6.txt','r')
cout = open('rosalind_ini6.out','w')


w = cin.read().split()

d = collections.defaultdict(int)
for i in w:
    d[i] = d[i]+1

for i in d:
    print >> cout, i,d[i]
    print i,d[i]
cin.close()
cout.close()
