import json
import yaml
from pathlib import Path
from gendiff.json import format_json
from gendiff.plain import format_plain
from gendiff.stylish import format_stylish
from gendiff.cli import parse_args


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def parse_content(content, file_format):
    if file_format == '.yml':
        return yaml.safe_load(content)
    elif file_format == '.json':
        return json.loads(content)


def parse_file(filename):
    content = read_file(filename)
    file_format = Path(filename).suffix
    return parse_content(content, file_format)


def build_diff(data1, data2):
    diff = []
    keys = sorted(data1.keys() | data2.keys())  

    for key in keys:
        if key not in data1:
            diff.append({"key": key, "type": "added", "value": data2[key]})
        elif key not in data2:
            diff.append({"key": key, "type": "removed", "value": data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                "key": key,
                "type": "nested",
                "children": build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({"key": key, "type": "unchanged", "value": data1[key]})
        else:
            diff.append({
                "key": key,
                "type": "changed",
                "old_value": data1[key],
                "new_value": data2[key]
            })
    return diff


def generate_diff(first_file, second_file, format_type='stylish'):
    diff = build_diff(parse_file(first_file), parse_file(second_file))

    if format_type == 'stylish':
        return format_stylish(diff)
    elif format_type == 'plain':
        return format_plain(diff)
    elif format_type == 'json':
        return format_json(diff)
