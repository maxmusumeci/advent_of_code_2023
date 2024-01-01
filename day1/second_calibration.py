# open file
# for each number in file
# add to count
# close file
#print count


def word_detection(linestr, letters):
  
  for j in range(len(letters)):
    if letters[j] in linestr:
      return j 
  
  return 0 

count = 0

letters = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

input_file = open("input.txt", 'r')
for line in input_file:
  num = 0
  dummy_val = 0
  linestr = ""
  for i in line:
    if i.isnumeric():
      num = int(i) * 10
      break
    else:
      linestr += i
      num = word_detection(linestr, letters)
      if num != 0:
        num = num * 10
        break
  linestr = ""
  for i in reversed(line):
    if i.isnumeric():
      num = num + int(i)
      break
    else:
      linestr += i
      dummy_val = word_detection(linestr[::-1], letters)
      if dummy_val != 0:
        num = num + dummy_val
        break
  count = count + num 

print(count)


