#Replica string

t = int(input())
for i in range(t):
    S = str(input())
    A = ""
    A += S 
    B = ""
    B += S[::-1]
    print(A)
    print(B)
