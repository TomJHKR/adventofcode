import os
import re 
import pprint
input = open("input.txt", "r")


all_lines = input.read()
lister = []

lister.append(re.findall("mul\([0-9]*,[0-9]*\)", all_lines))

def get_number(mul):
    string = mul.replace("mul(", "").replace(")","")
    splitter = string.split(",")
    num1 = splitter[0]
    num2 = splitter[1]
    return int(num1) * int(num2)

totals = 0
for item in lister:
    for mul in item:
        ans = get_number(mul)
        totals += ans

print(totals)

##Day 2

def is_do(chars):
    if chars[0] == "o" and chars[1] == "(" and chars[2] == ")":
        return True
    return False
## SOOOOO GROSS MY BAD 
def is_dont(chars):
    if chars[0] == "o" and chars[1] == "n" and chars[2] == "'" and chars[3] == "t" and chars[4] == "(" and chars[5] == ")":
        return True
    return False

new_defined = ""
read = True
for i in range(len(all_lines)):
    if read:
        new_defined += all_lines[i]
    if all_lines[i] == "d":
        if is_do(all_lines[i+1:i+4]):
            read = True
        elif is_dont(all_lines[i+1:i+7]):
            read = False

new_list = re.findall("mul\([0-9]*,[0-9]*\)", new_defined)

totals_2 = 0
for item in new_list:
    mynum = get_number(item)
    totals_2 += mynum

print(totals_2)
