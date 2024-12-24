from pathlib import Path

from gendiff.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff():
    file1_json = get_test_data_path('file1.json')
    file2_json = get_test_data_path('file2.json')
    file1_yml = get_test_data_path('file1.yml')
    file2_yml = get_test_data_path('file2.yml')
    result = read_file('result.txt')
    diff_json = generate_diff(file1_json, file2_json)
    diff_yml = generate_diff(file1_yml, file2_yml)

    assert result == diff_json
    assert result == diff_yml
