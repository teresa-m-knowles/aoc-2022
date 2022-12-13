with open('input.txt') as file: 
  pairs = file.read().split('\n')


fully_contained_pairs = 0
overlap = 0

for pair in pairs:
    first_assignment, second_assignment = list(map(lambda x: x.split('-'), pair.split(',')))
    start1 = int(first_assignment[0])
    end1 = int(first_assignment[1])
    start2 = int(second_assignment[0])
    end2 = int(second_assignment[1])

    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        fully_contained_pairs += 1

    if max(start1, start2) <= min(end1, end2):
        overlap += 1

print('One range fully contains the other in %s' %fully_contained_pairs)

print('There is overlap in %s pairs' %overlap)
