import argparse

from gendiff.gendiff import build_diff, parse_file
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output', default='stylish', choices=['stylish', 'plain'])
    args = parser.parse_args()

    diff = (build_diff(parse_file(args.first_file), parse_file(args.second_file)))

    if args.format == 'stylish':
        print(format_stylish(diff))
    if args.format == 'plain':
        print(format_plain(diff))


if __name__ == '__main__':
    main()
