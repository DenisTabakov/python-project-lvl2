#!/usr/bin/env python

from gendiff.differ import generate_diff
from gendiff.parser import choose_format


def main():
    file_1, file_2, output_format = choose_format()
    diff = generate_diff(file_1, file_2, output_format)
    print(diff)


if __name__ == '__main__':
    main()
