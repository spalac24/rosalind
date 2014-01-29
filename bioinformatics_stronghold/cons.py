from sys import stdin
dnas = ''.join([i.strip() if i[0]!='>' else '>' for i  in stdin.readlines()]).split('>')[1:]
joined=[''.join([s[x] for s in dnas]) for x in range(0,len(dnas[0]))]
letters = ['A','C','G','T']
mat = [[list(joined[j]).count(letters[i]) for j in range(0,len(joined))] for i in range(0,4)]
matp = [[mat[i][j] for i in range(0,len(mat))] for j in range(len(mat[0]))]

cons = ''.join([letters[matp[i].index(max(matp[i]))] for i in range(0,len(matp))])
print cons
for i in range(0,4):
    print str(letters[i])+":",' '.join(map(str,mat[i]))
