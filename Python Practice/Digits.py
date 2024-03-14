n = int(input())
n1 = n
m1 = 0

while n1 != 0:
    digi = n1 % 10  # fetching last digit of n1 
    if digi % 2 == 0:
        m1 = m1 * 10 + digi  # adding last digit of n1 to m1
    n1 //= 10  # removing digit from n1 

print(m1)  # printed the number removing odd digits.

sum = 0
n1 = n

while n1 != 0:
    digi = n1 % 10  # fetching last digit of n1 
    sum += digi  # adding last digit of n1 to sum
    n1 //= 10  # removing last digit of n1 

print(sum)
