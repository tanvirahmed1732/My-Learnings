# Keplers Law

t = int(input())
for i in range(t):
    t1, t2, r1, r2 = map(int,input().split())
    if (t1**2/r1**3) == (t2**2/r2**3):
        print('Yes')
    else:
        print('No')
