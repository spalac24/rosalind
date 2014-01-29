a = raw_input().strip()
b = raw_input().strip()

n = len(b)
for i in range(0,len(a)):
    if a[i:i+n] == b:
        print i+1,

