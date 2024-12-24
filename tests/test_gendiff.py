from pathlib import Path
from gendiff.gendiff import generate_diff

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff():
    file_1 = read_file('file1.json')
    file_2 = read_file('file2.json')
    result = read_file('result.txt')
    diff = generate_diff(file_1, file_2)

    assert result == diff
