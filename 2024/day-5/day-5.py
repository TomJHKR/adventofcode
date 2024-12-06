import os

input = open("test-input.txt", "r")

all = input.read().split("\n\n")
ordering_rules = all[0]
page_nums = all[1]
placeholder_good_pages = []
sum_part_1 = []
incorrect = dict()

def is_end(page,i):
    if len(page) > int(i):
        return True
    return False


def check_all(page,num,i):
    for rule in ordering_rules.split("\n"):
        both = rule.split("|")
        left = both[0]
        if is_end(page, i):
            right = both[1]
            if int(left) == int(num):
                if right in page:
                    index_left = page.index(left)
                    index_right = page.index(right)
                    if index_left > index_right:
                        flatter = ''.join(str(x) for x in page)
                        if flatter not in incorrect.keys() or len(incorrect) == 0:
                            temp_list = page
                            temp = temp_list[index_left]
                            temp_list[index_left] = temp_list[index_right]
                            temp_list[index_right] = temp
                            incorrect[flatter] = temp_list
                        return False
    
    return True

def per_num(page): 
    for i, num in enumerate(page):
        if not check_all(page, num, i):
            return False
    return True

for page in page_nums.split("\n"):
    if page != "":
        nums_in_page = page.split(",")
        if per_num(nums_in_page):
            middle = float(len(nums_in_page))/2
            sum_part_1.append(nums_in_page[int(middle - .5)])

total = 0
for number in sum_part_1:
    total += int(number)

print(total)

part_2_list = []
total_part2 = 0
for k,v in incorrect.items():
    print(k,v)
    middle = float(len(v))/2
    print(middle)
    part_2_list.append(v[int(middle - .5)])

for numnum in part_2_list:
    print(numnum)
    total_part2 += int(numnum)

print(total_part2)
