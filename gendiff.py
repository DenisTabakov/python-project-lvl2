import argparse
import json

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', metavar='first_file', help='')
parser.add_argument('second_file', metavar='second_file', help='')
parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')


def generate_diff(file_1, file_2):
    with open(file_1) as json_file_1:
        data_1 = json.load(json_file_1)

    with open(file_2) as json_file_2:
        data_2 = json.load(json_file_2)

    keys = data_1.keys() | data_2.keys()
    result = []
    for key in keys:
        if key not in data_1:
            res = f" + {key}: {data_2[key]}\n"
            result.append(res)
        elif key not in data_2:
            res = f" - {key}: {data_1[key]}\n"
            result.append(res)
        elif data_1[key] == data_2[key]:
            res = f"   {key}: {data_1[key]}\n"
            result.append(res)
        elif data_1[key] != data_2[key]:
            res_1 = f" - {key}: {data_1[key]}\n"
            res_2 = f" + {key}: {data_2[key]}\n"
            result.append(res_1)
            result.append(res_2)
        else:
            result.append('DANGER!!!')

    result.sort(key=lambda x: x[3])
    result.insert(0, '{\n')
    result.append('}')
    return ''.join(result)


if __name__ == '__main__':
    args = parser.parse_args()
