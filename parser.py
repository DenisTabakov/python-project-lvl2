import argparse
import os
import json
import yaml
from yaml.loader import SafeLoader


def choose_format():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', help='')
    parser.add_argument('second_file', metavar='second_file', help='')
    parser.add_argument('-f', '--format', metavar='FORMAT', default="stylish",
                        help='set format of output (default: "stylish")')
    parser.add_argument('-out', '--output', metavar='OUTPUT', default="txt",
                        help='output file extension')

    args = parser.parse_args()
    file_1 = args.first_file
    file_2 = args.second_file
    output_extension = args.output
    output_format = args.format

    filename_1, file_extension_1 = os.path.splitext(file_1)
    filename_2, file_extension_2 = os.path.splitext(file_2)

    if file_extension_1 == '.json' and file_extension_2 == '.json':
        with open(file_1) as f_1:
            data_1 = json.load(f_1)

        with open(file_2) as f_2:
            data_2 = json.load(f_2)

    elif (file_extension_1 == '.yaml' or file_extension_1 == '.yml')\
            and (file_extension_2 == '.yaml' or file_extension_2 == '.yml'):
        with open(file_1) as f_1:
            data_1 = yaml.load(f_1, Loader=SafeLoader)
        with open(file_2) as f_2:
            data_2 = yaml.load(f_2, Loader=SafeLoader)

    return data_1, data_2, output_format, output_extension
