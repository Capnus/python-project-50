import json

FILE1 = json.load(open('file1.json'))
FILE2 = json.load(open('file2.json'))
sort_FILE1 = dict(sorted(FILE1.items()))
sort_FILE2 = dict(sorted(FILE2.items()))


def generate_diff(file1, file2):
    res = ''
    for keys, values in file1.items():
        if keys in file2 and file1[keys] == file2[keys]:
            res += f'  {keys}: {values}' + '\n'
            file2.pop(keys)
            continue
        if keys in file2 and file1[keys] != file2[keys]:
            res += f'- {keys}: {values}' + '\n'
            res += f'+ {keys}: {file2[keys]}' + '\n'
            file2.pop(keys)
            continue
        if keys not in file2:
            res += f'- {keys}: {values}' + '\n'
            continue
    for keys2, values2 in file2.items():
        if keys2 not in file1:
            res += f'- {keys2}: {values2}' + '\n'
    return res


__all__ = ['generate_diff']
