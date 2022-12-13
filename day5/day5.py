import re
import copy

with open('input.txt') as file: 
  s = file.read()
  char_after_column = re.search(r" \n\nmove", s).start()
  text = s[0:char_after_column]
  no_of_columns = int(re.findall('[0-9]+', text)[-1])

  m = re.search(r"\n 1", s).start()
  chunk_with_crates= s[0:m]
  crates = chunk_with_crates.split('\n')

  columns = [[] for i in range(no_of_columns)]

  for line in crates:
    a = line.replace('] ', '').replace(' [', '').replace('[', '').replace(']', '')
    test = list(a.replace('   ', 'X').replace(' ', ''))

    for col, value in enumerate(test):
        this_column = columns[col]
        if value != 'X':
            this_column.append(value)
  
  for col in columns:
    col = col.reverse()
  
  columns_two = copy.deepcopy(columns)

  start_of_instructions = s[char_after_column:]

  moves = start_of_instructions.strip().split('\n')

  for move in moves:
    numbers = re.findall('[0-9]+', move)
    crates_to_move, giving_column, receiving_column = list(map(int, numbers))

    while crates_to_move > 0:
        moving_crate = columns[giving_column - 1].pop()
        columns[receiving_column - 1].append(moving_crate)
        crates_to_move = crates_to_move - 1
    
  resulting_string = ''

  for col in columns:
    resulting_string = resulting_string + col[-1]

print('The resulting string is %s' %resulting_string)


# PART TWO 

second_string = ''

for move in moves:
    numbers = re.findall('[0-9]+', move)
    crates_to_move, giving_column_number, receiving_column_number = list(map(int, numbers))
    giving_column = columns_two[giving_column_number - 1]
    receiving_column = columns_two[receiving_column_number -1]
    crates = giving_column[-crates_to_move:]
    del giving_column[-crates_to_move:]
    receiving_column.extend(crates)

for col in columns_two:
    second_string = second_string + col[-1]

print('The resulting string is %s' %second_string)