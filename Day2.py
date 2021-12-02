def pathFinder(filepath):
    horizontal = 0
    vertical = 0

    with open(filepath, 'r') as file_object:
        content = file_object.read().split('\n')
        for position, line in enumerate(content):
            current_line = line.split(' ')
            if current_line[0] == 'up':
                vertical += int(current_line[1])
            elif current_line[0] == 'down':
                vertical -= int(current_line[1])
            elif current_line[0] == 'forward':
                horizontal += int(current_line[1])
    return horizontal, vertical

def pathFinderAim(filepath):
    aim = 0
    horizontal = 0
    vertical = 0

    with open(filepath, 'r') as file_object:
        content = file_object.read().split('\n')
        for position, line in enumerate(content):
            current_line = line.split(' ')
            if current_line[0] == 'up':
                aim -= int(current_line[1])
            elif current_line[0] == 'down':
                aim += int(current_line[1])
            elif current_line[0] == 'forward':
                horizontal += int(current_line[1])
                vertical += (aim * int(current_line[1]))
    return horizontal, vertical


if __name__ == '__main__':
    horizontal, vertical = pathFinderAim('day2.txt')
    print(horizontal, vertical)
    print(horizontal * vertical)
