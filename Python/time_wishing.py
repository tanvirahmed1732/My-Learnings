import time
timestamp = time.strftime("%H:%M:%S")
# print(type(timestamp))
print(timestamp)
hour = int(time.strftime("%H"))
if(hour<12):
  print("Good Morning")
elif(hour<18):
  print("Good Noon")
else:
  print("Good Night")