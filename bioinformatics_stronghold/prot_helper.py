
lines = [i.strip() for i in open('prot_table.py','r')]
words = " ".join([" ".join(i.split())for i in lines]).split()
i = 0
print '{',
while i < len(words):
    print '\"'+words[i]+'\"',":",'\"'+words[i+1]+'\"',","
    i += 2
print '}'
