
cin = open('rosalind_gc.txt','r')

def count_gc(s):
    return float(len(filter((lambda x:  x == 'G' or x == 'C'),s)))/len(s)



linesp = [i.strip() for i in cin.readlines()]
lines = [linesp[0]]
acum = ""
for v in linesp[1:]:
    if (list(v)[0]=='>'):
        lines.append(acum)
        lines.append(v)
        acum = ""
    else:
        acum += v
lines.append(acum)

it = 0

best = ""
gc = 0.0
while it < len(lines):
    nbest = count_gc(lines[it+1])
    if (nbest > gc):
        gc = nbest
        best = lines[it][1:]
    it += 2

print best,gc*100
cin.close()
