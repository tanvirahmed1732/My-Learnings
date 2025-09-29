que = ["Which one is not a programming language?", "Can overwrite elements of tuple in Python?", "String is ....... in Python", "In tuple which method is not applicable directly?", "Is there any do while loop availabe in Python?", "Which method return a value?", "Which method can modify the original list?"]
opt = ['Java', 'Python', 'HTML', 'C', 'No', 'I don\'t know', 'What is tuple?', 'Yes', 'List', 'String', 'Immutable', 'Enemy', 'count()', 'index()', 'What are you talking about?', 'append()', 'Yes', 'No', 'I am confused', 'Never heard about this.', 'sort()', 'index()', 'extend()', 'insert()', 'count()', 'copy()', 'sort()', 'index()']
ans = [3, 1, 3, 4, 2, 2, 3]
count = 0
n = 0;
w = 'Welcome to KBC'
print(w.center(50, '*'))
print()
print("Here is your questions: ", '\n')
while(n<7):
  print(que[n])
  k = n*4
  j = 1
  for i in range(k,k+4):
    print(j,': ', opt[i], sep='')
    j = j + 1
  option = int(input('Choose an option: '))
  if option is ans[n]:
    count = count + 1
    print('You are right \n', 'You won: ', count, 'cr', sep='')
  else:
    print('Your answer is wrong \n', 'Take: ', count, 'cr and...', sep ='')
    print('Goodbye')
    break
  print()
  n = n + 1