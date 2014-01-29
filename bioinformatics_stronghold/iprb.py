from sys import stdin

a,b,c = map(float,stdin.readline().split())
suma = a+b+c
probr = c/suma*((c-1)/(suma-1)+0.5*b/(suma-1))+b/suma*(0.5*c/(suma-1)+0.25*(b-1)/(suma-1))
print 1.0-probr
