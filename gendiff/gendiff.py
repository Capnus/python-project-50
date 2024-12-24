import copy
import json
from pathlib import Path

import yaml


def parse_file(filename):
    with open(filename) as file:
        if Path(filename).suffix == '.yml':
            return yaml.safe_load(file)
        elif Path(filename).suffix == '.json':
            return json.load(file)
        

def generate_diff(path_to_file1, path_to_file2):
    file1 = parse_file(path_to_file1)
    file2 = parse_file(path_to_file2)
    copy_file1 = copy.deepcopy(file1)
    copy_file1.update(file2)
    sorted_dict = dict(sorted(copy_file1.items()))
    res = ''
    for keys, values in sorted_dict.items():
        if keys in file1 and keys in file2:
            if file1[keys] == file2[keys]:
                res += f'  {keys}: {values}\n'
            else:
                res += f'- {keys}: {file1[keys]}\n'
                res += f'+ {keys}: {file2[keys]}\n'
        if keys in file1 and keys not in file2:
            res += f'- {keys}: {file1[keys]}\n'
        if keys in file2 and keys not in file1:
            res += f'+ {keys}: {file2[keys]}\n'
    return res[:-1]
