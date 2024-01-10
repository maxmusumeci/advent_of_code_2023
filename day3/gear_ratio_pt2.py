def in_gear_list(row, col):
  return (row, col) in gear_list

def check_adjacent(row, col):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            new_row, new_col = row + i, col + j
            if (0 <= new_col < num_cols) and (0 <= new_row < num_rows):
                pos = gear_map[new_row][new_col]
                if (pos.isdigit()):
                     
    return False

count = 0
is_num = False
is_symbol = False
gear_map = []
gear_list = []
# gear_list.append((new_row, new_col))
#if  in_gear_list(new_row, new_col):

with open("sample1.txt", 'r') as input_file:
    for line in input_file:
        line = line.rstrip('\n')
        gear_map.append(line)

num_rows = len(gear_map)
num_cols = len(gear_map[0]) if gear_map else 0
gear = ""

for row in range(num_rows):
  for col in range(num_cols):
    print(gear_map[row][col], end="")
  print()

for row_index in range(num_rows):
    for col_index in range(num_cols):
        if gear_map[row_index][col_index] == '*':
            is_num = check_adjacent(row_index, col_index)
        elif is_num:
            if is_symbol:
                count += int(gear)

            gear = ""
            is_num = 0
            is_symbol = False
print(gear_list)
#print(count)
