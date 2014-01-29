cin = open('rosalind_hamm.txt','r')

a = list(cin.readline().strip())
b = list(cin.readline().strip())


ans = 0
for i in range(0,len(a)):
    if a[i] != b[i]:
        ans += 1

print ans
