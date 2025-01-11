import json
import yaml
from pathlib import Path
from gendiff.json import format_json
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish

def read_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()

def parse_content(content, file_extension):
    file_extension = file_extension.lower()  

    if file_extension == '.yml' or file_extension == '.yaml':
        return yaml.safe_load(content)
    elif file_extension == '.json':
        return json.loads(content)


def parse_file(filename):
    content = read_file_content(filename)
    file_extension = Path(filename).suffix
    return parse_content(content, file_extension)


def build_diff(data1, data2):
    keys = sorted(list({**data1, **data2}.keys()))
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = {
                'status': 'added',
                'value': data2[key],
            }
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'value': data1[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'status': 'unchanged',
                'value': build_diff(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            diff[key] = {
                'status': 'unchanged',
                'value': data2[key]
            }
        else:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return diff


def generate_diff(first_file, second_file, format_type='stylish'):
    diff = build_diff(parse_file(first_file), parse_file(second_file))

    if format_type == 'stylish':
        return format_stylish(diff)
    elif format_type == 'plain':
        return format_plain(diff)
    elif format_type == 'json':
        return format_json(diff)
