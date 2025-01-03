from pathlib import Path

from gendiff.gendiff import build_diff, parse_file
from gendiff.json import format_json
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff():
    file1_json = get_test_data_path('file1.json')
    file2_json = get_test_data_path('file2.json')
    file1_yml = get_test_data_path('file1.yml')
    file2_yml = get_test_data_path('file2.yml')
    
    result_plain = read_file('result_plain.txt')
    result_stylish = read_file('result.txt')
    result_json = read_file('result_json.txt')

    diff_json_plain = format_plain(
        build_diff(parse_file(file1_json), parse_file(file2_json))
        )
    diff_yml_plain = format_plain(
        build_diff(parse_file(file1_yml), parse_file(file2_yml))
        )
    
    diff_json_stylish = format_stylish(
        build_diff(parse_file(file1_json), parse_file(file2_json))
        )
    diff_yml_stylish = format_stylish(
        build_diff(parse_file(file1_yml), parse_file(file2_yml))
        )

    diff_json_json = format_json(
        build_diff(parse_file(file1_json), parse_file(file2_json))
        )
    diff_yml_json = format_json(
        build_diff(parse_file(file1_yml), parse_file(file2_yml))
        )

    assert result_plain == diff_json_plain
    assert result_plain == diff_yml_plain

    assert result_stylish == diff_json_stylish
    assert result_stylish == diff_yml_stylish

    assert result_json == diff_json_json
    assert result_json == diff_yml_json