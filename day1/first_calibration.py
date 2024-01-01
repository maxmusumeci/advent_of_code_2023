
# open file
# for each number in file
# add to count
# close file
#print count

count = 0

input_file = open("input.txt", 'r')
for line in input_file:
  num = 0 
  for i in line:
    if i.isnumeric():
      num = int(i) * 10
      break
  for i in reversed(line):
    if i.isnumeric():
      num = num + int(i)
      break

  count = count + num 

print(count)


