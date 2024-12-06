import os
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageSequenceClip
global current_pos

## ROW, COL
UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

S_LEFT = "<"
S_UP = "^"
S_DOWN = "v"
S_RIGHT = ">"

ORDER = [UP,RIGHT,DOWN,LEFT]
matrix = [list(sub.strip()) for sub in open("input.txt", "r").readlines()]
mapped = matrix
frames = []

# Get grid size
rows_size = len(matrix)
cols_size = len(matrix[0])

def animate2():
    global current_pos
    sleep(0.15)
    os.system('clear')  # Clear screen on every update
    for row in matrix:
        colored_row = ""
        for cell in row:
            if cell == "^" or cell == "v" or cell == "<" or cell == ">":  # Guard symbol
                colored_row += "\033[41m" + cell + "\033[0m"  # Red
            elif cell == "#":  # Obstacle
                colored_row += "\033[44m" + cell + "\033[0m"  # Green
            elif cell == "X":  # Visited position
                colored_row += "\033[47m" + cell + "\033[0m"  # Yellow
            else:
                colored_row += cell  # Default (no color)
        print(colored_row)

def animate():
    global current_pos
    cell_size = 5
    img = Image.new('RGB', (cols_size * cell_size, rows_size * cell_size), color='black')  
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 16)  
    except IOError:
        font = ImageFont.load_default()

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == ".":
                cell = ""
            x = j * cell_size  # 20px per cell horizontally
            y = i * cell_size  # 20px per cell vertically
            bg_color = "black"
            text_color = "white"
            if cell in [S_UP, S_DOWN, S_LEFT, S_RIGHT]:
                cell = ""
                bg_color = "royalblue"
            elif cell == "#":
                cell = ""
                bg_color = "firebrick"
            elif cell == "X":
                cell = ""
                bg_color = "lightgray"

            # Draw background rectangle
            draw.rectangle([x, y, x + cell_size, y + cell_size], fill=bg_color)
            # Draw the text
            draw.text((x + cell_size // 4, y + cell_size // 4), cell, fill=text_color, font=font)

    img = img.resize((img.width * 2, img.height * 2), Image.Resampling.LANCZOS)
    img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)
    # Append the frame to the frame list
    img.save(f'frame_{len(frames)}.png')
    frames.append(f'frame_{len(frames)}.png')  # Track the frame file path


def get_symbol(step):
    step = str(step)
    if step == str(UP):
        return S_UP
    elif step == str(DOWN):
        return S_DOWN
    elif step == str(LEFT):
        return S_LEFT
    elif step == str(RIGHT):
        return S_RIGHT

def is_blocked(step):
    check_blocked = matrix[current_pos[0]+step[0]][current_pos[1]+step[1]]
    if check_blocked == "#":
        return True
    return False

def guard_gone(direction):
    try:
        test = (current_pos[0]+direction[0],current_pos[1]+direction[1])
        test_square = matrix[test[0]][test[1]]
        return True
    except:
        return False

def move(step):
    global current_pos
    if not guard_gone(step):
        print("Outside")
        return "DONE"
    
    to_add = matrix[current_pos[0]][current_pos[1]]
    if to_add != "X":
        matrix[current_pos[0]][current_pos[1]] = "X"

    is_block = is_blocked(step)
    if not is_block:
        current_pos = ((current_pos[0]+step[0]),(current_pos[1]+step[1]))
        matrix[current_pos[0]][current_pos[1]] = get_symbol(step)
        return "MOVE"
    else:
        return "CHANGE"

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == "^":
            starting_pos = (row,col)
            current_pos = (row,col)

# Create a list to store frames

print(starting_pos)
direction = 0
while True:
    animate()
    outcome = move(ORDER[direction])
    match outcome:
        case "DONE":
            break
        case "CHANGE":
            direction += 1
    if direction == 4:
        direction = 0

# Create a video from saved frames
clip = ImageSequenceClip([f'frame_{i}.png' for i in range(len(frames))], fps=120)
clip.write_videofile("animation.mp4", codec="libx264",bitrate="1M")
# Clean up intermediate PNG files
for i in range(len(frames)):
    os.remove(f'frame_{i}.png')
print("GIF generated successfully!")
count = sum(row.count('X') for row in matrix)
print(count)


