import argparse
import json
import yaml
from yaml.loader import SafeLoader


def parse(file):
    if file.endswith(".json"):
        data = json.load(open(file))
    elif file.endswith((".yaml", ".yml")):
        with open(file) as f:
            data = yaml.load(f, Loader=SafeLoader)
    elif file.endswith(".txt"):
        with open(file) as f:
            data = f.read()
    return data


def choose_format():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', help='')
    parser.add_argument('second_file', metavar='second_file', help='')
    parser.add_argument('-f', '--format', metavar='FORMAT', default="stylish",
                        help='set format of output (default: "stylish")')
    parser.add_argument('-out', '--output', metavar='OUTPUT', default="None",
                        help='output file extension')

    args = parser.parse_args()
    file_1 = args.first_file
    file_2 = args.second_file
    output_extension = args.output
    output_format = args.format

    data_1 = parse(file_1)
    data_2 = parse(file_2)

    return data_1, data_2, output_format, output_extension
