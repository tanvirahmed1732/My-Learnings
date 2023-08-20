def prime(a):
  if(a==0 or a==1):
    print("Not Prime")
    return
  check = False
  for i in range(2, int(a/2)+1):
    if(a%i==0):
      check = True
      break;
  if(check == False):
    print("Prime")
  else:
    print("Not Prime")

while True:
  n = int(input()`)
  prime(n)