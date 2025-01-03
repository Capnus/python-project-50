import json
from pathlib import Path

import yaml


def parse_file(filename):
    with open(filename) as file:
        if Path(filename).suffix == '.yml':
            return yaml.safe_load(file)
        if Path(filename).suffix == '.json':
            return json.load(file)


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