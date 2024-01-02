
# semicolon delimmited
# s.strip().split(';') should split string into an array of strings
# separated by ; or newline character while also deleting the \n char

max_val = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
    }

input_file = open("input.txt", 'r')
for line in input_file:
  game_id, contents = line.split(":")
  game_id = game_id.split()[1]
  
  round_id = contents.split(";")
  round_id = [i.strip() for i in round_id]

  for i, rnd in enumerate(round_id):
    cube_val, color = round_id[i].split(",")[i].split()
    print(cube_val)
    print(color)


