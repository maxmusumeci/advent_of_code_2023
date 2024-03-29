
# semicolon delimmited
# s.strip().split(';') should split string into an array of strings
# separated by ; or newline character while also deleting the \n char

max_val = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
    }

count = 0

input_file = open("input.txt", 'r')
for line in input_file:
  valid_game = 1
  game_id, contents = line.split(":")
  game_id = game_id.split()[1]
  
  round_id = contents.split(";")
  round_id = [i.strip() for i in round_id]
  
  for rnd in round_id:
    rnd = rnd.strip()
    cubes = rnd.split(",")
    for cube in cubes:
      cube_num, color = cube.strip().split()
      if int(cube_num) > max_val[color]:
        valid_game = valid_game * 0
      else:
        valid_game = valid_game * 1
  if valid_game == 1:
    count = count + int(game_id)
    print(game_id)

  '''for i in enumerate(round_id):
    #print(cube_val)
    rnd = round_id[i].split(",")
    for j in rnd:
      cube_num, color = round_id[i].split(",")[j].split()
      print(cube_num)
      print(color)

'''
print(count)
