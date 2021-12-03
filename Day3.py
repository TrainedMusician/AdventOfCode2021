import numpy as np


def arrayGenerator(filepath):
    numeric_content = []
    with open(filepath, 'r') as file_object:
        content = file_object.read().split('\n')
        for position, line in enumerate(content):
            current_line = []
            for character in line:
                current_line.append(int(character))
            numeric_content.append(current_line)
    return np.array(numeric_content)


def powerConsumptionExtractor(data):
    halved_length = len(data) // 2
    gamma = ''
    epsilon = ''
    for position in range(data.shape[1]):
        if np.count_nonzero(data[:, position]) > halved_length:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return gamma, epsilon


def oxygenExtractor(data):
    halved_length = len(data) // 2
    for position in range(data.shape[1]):
        indexes = np.where(data[:, position] == 1)
        if len(indexes[0]) >= halved_length:
            print('More %s' % indexes)
        else:
            indexes = np.where(data[:, position] == 0)
        data = data[indexes]
        halved_length = len(data) // 2 + len(data) % 2
        if len(data) == 1:
            break
    return ''.join(list(data[0].astype(str)))


def CO2Extractor(data):
    halved_length = len(data) // 2
    for position in range(data.shape[1]):
        indexes = np.where(data[:, position] == 1)
        if len(indexes[0]) < halved_length:
            print('More %s' % indexes)
        else:
            indexes = np.where(data[:, position] == 0)
        data = data[indexes]
        halved_length = len(data) // 2 + len(data) % 2
        if len(data) == 1:
            break
    return ''.join(list(data[0].astype(str)))


def binaryToDecimal(value):
    decimal_value = 0
    total_length = len(value)
    for position in range(total_length):
        if value[position] == '1':
            decimal_value += (1 << (total_length - position - 1))
    return decimal_value


if __name__ == '__main__':
    content_array = arrayGenerator('day3.txt')
    # gamma, epsilon = powerConsumptionExtractor(content_array)
    # print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))

    print(binaryToDecimal(oxygenExtractor(content_array)) * binaryToDecimal(CO2Extractor(content_array)))
