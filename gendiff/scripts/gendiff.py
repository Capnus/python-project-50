<<<<<<< HEAD
from gendiff.gendiff import generate_diff
from gendiff.cli import parse_args
=======
from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff

>>>>>>> 18d89392f3be05214cf82c050f886f2099efb52a

def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
