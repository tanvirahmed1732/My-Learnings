# Output all digits of a number

t = int(input())
for i in range(t):
    #declare N as a string instead of an integer
    N = str(input())        
    
    #list to hold all digits of the number
    final_ans = []          
    
    #useful string syntax
    for i in N:             
        final_ans.append(i)
        
    print(*final_ans)
