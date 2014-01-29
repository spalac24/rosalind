n,m = map(int,raw_input().split())

alive = [[0]*m]*n
alive = [[0 for x in range(0,m)] for y in range(0,n)]
    
alive[0][0] = 1
for i in range(1,n):
    for j in range(1,m):
        alive[i][j] = alive[i-1][j-1]
        alive[i][0] += alive[i-1][j]


print sum(alive[n-1])

