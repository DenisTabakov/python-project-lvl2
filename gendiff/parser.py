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

    args = parser.parse_args()
    file_1 = args.first_file
    file_2 = args.second_file
    output_format = args.format

    return file_1, file_2, output_format
