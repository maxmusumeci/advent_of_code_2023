# Gear Ratio
# iterate accross a "2-D plane" of numbers and symbols, check if
# character is a number, and if so, while the next symbols are numbers,
# check if there is a "special  symbol" adjacent to it
# if there is, then add it to the part number once the number completes
# we need to detect when a number starts, when it finishes, and copy the number in case we want to add it to the sum

def check_adjacent(row, col):
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (col + j >= num_cols or col + j < 0) or (row + i >= num_rows or row + i < 0):
        continue
      pos = gear_map[row + i][col + j]
      if not (pos.isdigit() or pos == '.'):
        return True

  return False

count = 0
is_num = 0
is_symbol = False
gear_map = []
input_file = open("input.txt", 'r')
num_rows = 140 # arbitrary from input text
num_cols = 140 # arbitrary from input text
gear = ""

# read gearmap
for line in input_file:
  line = line.rstrip('\n') # strip newline char
  gear_map.append(line)

input_file.close()

for i in range(num_rows):
  for j in range(num_cols):
    if gear_map[i][j].isdigit():
      is_num = 1
      gear += gear_map[i][j] 
      is_symbol = check_adjacent(i, j)
    elif is_num:
      if is_symbol:
        count = count + int(gear)

      gear = ""
      is_num = 0

print(count)



#print(j, end="")

