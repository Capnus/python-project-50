from pathlib import Path

import pytest

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path('tests/test_data') / filename


def read_file(filename):
    path = get_test_data_path(filename)
    return path.read_text()


@pytest.mark.parametrize(
    "file1, file2, result_file, format_name",
    [
        ('file1.json', 'file2.json', 'result.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'result.txt', 'stylish'),
        ('file1.json', 'file2.json', 'result_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'result_plain.txt', 'plain'),
        ('file1.json', 'file2.json', 'result_json.txt', 'json'),
        ('file1.yml', 'file2.yml', 'result_json.txt', 'json'),
    ],
    ids=[
        "json_stylish", "yaml_stylish", 
        "json_plain", "yaml_plain", 
        "json_json", "yaml_json", 
    ]
)


def test_generate_diff(file1, file2, result_file, format_name):
    file1_path = get_test_data_path(file1)
    file2_path = get_test_data_path(file2)

    expected_result = read_file(result_file)

    diff = generate_diff(file1_path, file2_path, format_name)

    assert expected_result == diff
