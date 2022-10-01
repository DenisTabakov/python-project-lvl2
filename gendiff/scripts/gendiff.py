#!/usr/bin/env python

from engine.generate_diff import generate_diff


def main():
    diff = generate_diff()
    print(diff)


if __name__ == '__main__':
    main()