from pathlib import Path

import pytest

from gendiff.gendiff import build_diff, parse_file
from gendiff.json import format_json
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish


def get_test_data_path(filename):
    return Path('tests/test_data') / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.mark.parametrize(
    "file1, file2, result_file, formatter",
    [
        ('file1.json', 'file2.json', 'result_plain.txt', format_plain),
        ('file1.yml', 'file2.yml', 'result_plain.txt', format_plain),
        ('file1.json', 'file2.json', 'result.txt', format_stylish),
        ('file1.yml', 'file2.yml', 'result.txt', format_stylish),
        ('file1.json', 'file2.json', 'result_json.txt', format_json),
        ('file1.yml', 'file2.yml', 'result_json.txt', format_json),
    ]
)
def test_gendiff(file1, file2, result_file, formatter):
    file1_path = get_test_data_path(file1)
    file2_path = get_test_data_path(file2)
    result = read_file(result_file)

    diff = formatter(build_diff(parse_file(file1_path), parse_file(file2_path)))

    assert result == diff
