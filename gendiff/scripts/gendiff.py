import argparse

from gendiff.gendiff import build_diff, parse_file
from gendiff.stylish import format_stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(format_stylish(build_diff(parse_file(args.first_file), parse_file(args.second_file))))


if __name__ == '__main__':
    main()
