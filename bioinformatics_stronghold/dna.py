import collections

s = raw_input()
cout = open('rosalind_dna.out','w')

d = collections.defaultdict(int)

for c in s:
    d[c] += 1

v = " ".join(map(str,[d['A'],d['C'],d['G'],d['T']]))

print >> cout, v
print v

cout.close()
