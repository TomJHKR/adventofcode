import os



def test_nums(num1, num2):
    sum = abs(int(num1)-int(num2))
    if sum > 3 or sum == 0:
        return False
    return True

# Safety is the state of being protected from harm or danger.
# It can also refer to a device that prevents a machine or weapon from being used in a hazardous or accidental way
def determine_saftey(num1,num2,direction):
    if direction == "ASC" and num1 > num2:
        return False
    if direction == "DSC" and num1 < num2:
        return False
    if not test_nums(num1,num2):
        return False
    return True



safe_plus_list = []
input = open("input.txt", "r")

# when soliders go to lay, we give them one last fighting chance
def redemption(numms):
    length = len(numms)
    safe = True
    num0 = int(numms[0])
    num1 = int(numms[1])
    typ = ""
    if num0 == num1:
        safe = False
    elif num0 - num1 > 0:
        typ = "DSC"
    else:
        typ = "ASC"
    for i in range(length - 1):
        first = int(numms[i])
        second = int(numms[i+1])
        if not determine_saftey(first, second, typ):
            safe = False
            continue
    if safe:
        safe_plus_list.append(numms)


# This is my list for keeping track of part 1 passes 
safe_list = []

# kinda main but incorporates part 2
def main():
    for line in input.readlines():
        nums = line.split()
        length = len(nums)
        safe = True
        redemption_attempted = False
        num0 = int(nums[0])
        num1 = int(nums[1])
        typ = ""
        if num0 == num1:
            safe = False
            if not redemption_attempted:
                redemption(nums[1:-1])
            continue
        elif num0 - num1 > 0:
            typ = "DSC"
        else:
            typ = "ASC"
        for i in range(length - 1):
            first = int(nums[i])
            second = int(nums[i+1])
            if not determine_saftey(first, second, typ):
                safe = False
                if not redemption_attempted:
                    a = [x for y,x in enumerate(nums) if y != i]
                    redemption(a)
                    redemption_attempted = True
                continue
        if safe:
            safe_list.append(line)
    ## Works for me for some reason????
    ## You have got so far solider that you deserve to be appened to the list o7
    if nums not in safe_plus_list or nums not in safe_list:
        safe_plus_list.append(nums)
    print(f"""Amount Safe : {len(safe_list)}""")
    print(f"""Amount Safe 2 : {len(safe_plus_list) + len(safe_list)}""")


if __name__ == "__main__":
    main()
