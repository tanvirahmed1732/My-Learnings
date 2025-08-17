lst=list(map(int,input("Enter Some Positive Nonzero Numers (Space Seperated): ").split()))
odd,even=0,0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Odd Numbers:", odd,"\n""Even Numbers:", even)