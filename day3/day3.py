#  the last value in range is not included

def assign_priorities(priorities, first_letter, last_letter):
    for n in range(ord(first_letter), ord(last_letter) + 1):
        priorities[chr(n)] = len(priorities) + 1
    
    return priorities
    

priorities_of_items = {}

priorities_of_items = assign_priorities(priorities_of_items, "a", "z")
priorities_of_items = assign_priorities(priorities_of_items, "A", "Z")


with open('input.txt') as file: 
  rucksacks = file.read().split('\n')


running_balance = 0


for rucksack in rucksacks:
    size = len(rucksack) // 2
    first = list(rucksack[0:size])
    second = list(rucksack[-size:])
    intersection = list(set(first).intersection(second))[0]
    running_balance += priorities_of_items[intersection]


print("The total of priorities is %s" %running_balance)


# PART TWO

groups = []

running_total_two = 0

for n in range(0, len(rucksacks), 3):
    group = rucksacks[n: n+3]
    groups.append(group)

for group in groups:
    intersection = set(group[0]).intersection(group[1], group[2])
    intersection = list(intersection)[0]
    running_total_two += priorities_of_items[intersection]


print("The second total is %s" %running_total_two)