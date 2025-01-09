import argparse

from gendiff.gendiff import build_diff, parse_file
from gendiff.json import format_json
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish', choices=['stylish', 'plain', 'json']
                        )
    return parser.parse_args()


def generate_diff(first_file, second_file, format_type):
    diff = build_diff(parse_file(first_file), parse_file(second_file))

    if format_type == 'stylish':
        return format_stylish(diff)
    elif format_type == 'plain':
        return format_plain(diff)
    elif format_type == 'json':
        return format_json(diff)


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
