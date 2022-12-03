
with open('input.txt') as file: 
   chunks = file.read().split('\n\n')

calories_per_elf = []
for chunk in chunks:
    total_cals_per_elf= sum(list(map(int, chunk.split('\n'))))
    calories_per_elf.append(total_cals_per_elf)

calories_per_elf.sort(reverse = True)

most_calories_of_elves = max(calories_per_elf)
total_calories_top_three_elves = sum(calories_per_elf[0:3])
print(most_calories_of_elves)
print(total_calories_top_three_elves)
