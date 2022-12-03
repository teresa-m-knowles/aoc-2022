# Me:
# X --> Rock 1
# Y --> Paper 2
# Z --> Scissors 3

# Opponent
# A --> Rock
# B --> Paper
# C --> Scissors

# 3 draw 
# 0 lost
# 6 win 

# A Y
# B X
# C Z

# A -- beats: Z
#   -- draws: X
#   -- loses: Y

running_score = 0

rock = {'beats': ['Z', 'C'], 'loses': []}

# my move against 
rules = {
   'A': {'B': 1, 'C': 7, 'A': 4},
   'B': {'A': 8, 'B': 5, 'C': 2},
   'C': {'A': 3, 'B': 9, 'C': 6}
}

with open('input.txt') as file: 
   text = file.read()
   rounds = text.replace('Y', 'B').replace('X', 'A').replace('Z', 'C').replace(' ', '').split('\n')
   

for round in rounds:
   opp_move = round[0]
   my_move = round[1]
   running_score += rules[my_move][opp_move]


print(running_score)


# part two 

# X --> lose
# Y --> draw
# Z --> win

running_score_two = 0
# outcome we need vs what to 
rules_two = {
   'X': {'A': 3, 'B': 1, 'C': 2},
   'Y': {'A': 4, 'B': 5, 'C': 6},
   'Z': {'A': 8, 'B': 9, 'C': 7}
}

rounds_two = text.replace(' ', '').split('\n')

for round in rounds_two:
   opp_move = round[0]
   my_outcome = round[1]
   running_score_two += rules_two[my_outcome][opp_move]

print('The second running score is now % s' % running_score_two)
