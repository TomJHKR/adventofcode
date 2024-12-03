import os


input = open("input.txt", "r")

left = []
right = []

## Read lines and append to left and right list
for line in input.readlines():
    splitline = line.split()
    left.append(splitline[0])
    right.append(splitline[1])

## Part 1
total = 0
left.sort()
right.sort()
for i in range(len(left)):
    total += abs(int(left[i]) - int(right[i]))

## Part 1 answer
print(total)


## Part 2
## Store list of lefts with no dupes
nodupes = list(dict.fromkeys(left))

part_2_total = 0
for num in nodupes:
    part_2_total += int(num) * right.count(num)

print(part_2_total)


