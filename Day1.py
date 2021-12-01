def depthChecker(filepath):
    decreasing = 0
    increasing = 0

    with open(filepath, 'r') as file_object:
        content = file_object.read().split('\n')
        for position, line in enumerate(content):
            if position == 0:
                continue
            if int(line) > int(content[position-1]):
                increasing += 1
            elif int(line) < int(content[position-1]):
                decreasing += 1
            # print('%s, %s, %d, %d' % (content[position - 1], line, decreasing, increasing))
    return decreasing, increasing


def depthCheckerSliding(filepath):
    decreasing = 0
    increasing = 0

    with open(filepath, 'r') as file_object:
        content = [int(x) for x in file_object.read().split('\n')]
        for position, line in enumerate(content, start=1):
            if position < 4:
                continue
            # print(content[position - 3:position])

            # print('%s vs %s' % (sum(content[position - 3:position]), sum(content[position - 4:position - 1])))
            if sum(content[position - 3:position]) > sum(content[position - 4:position - 1]):
                increasing += 1
            if sum(content[position - 3:position]) < sum(content[position - 4:position - 1]):
                decreasing += 1
            # print('%d, %d' % (decreasing, increasing))
    return decreasing, increasing


if __name__ == '__main__':
    print(depthCheckerSliding('day1.txt'))
