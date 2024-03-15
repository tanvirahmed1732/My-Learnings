n = int(input())
n1 = n
m1 = 0

while n1 != 0:
    digi = n1 % 10  # fetching last digit of n1 
    if digi <= 5:
        m1 = m1 * 10 + digi  # adding last digit of n1 to m1
    n1 //= 10  # removing digit from n1 

print(m1)  # printed the number removing digits greater than 5.

product = 1
n1 = n

while n1 != 0:
    digi = n1 % 10  # fetching last digit of n1 
    product *= digi  # multiplying last digit of n1 to product
    n1 //= 10  # removing last digit of n1 

print(product)
