#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

from random import choice
def fight(a, b):
  win = [['d','l','w'],['w','d','l'],['l','w','d']]
  for i in win:
    if(win.index(i) == a):
      # print(i[b])
      return i[b]
while True:
 com = [0,1,2]
 c = choice(com)
 user = int(input("Enter your choice (0 for snake, 1 for water, 2 for gun or enter any other number for exit): "))
 if (user<0 or user>2):
    exit()
 if c == 0:
   print('Computer choise is: snake')
 elif c == 1:
   print('Computer choise is: water')
 else:
   print('Computer choice is: gun')
 check = str(fight (c, user))
 # print(check)
 print("Draw") if check == 'd' else print("Lose") if check == 'l' else print("Win")
 print()