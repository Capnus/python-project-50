def format_plain(diff, parent_key=''):
    lines = []
    for key, value in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        status = value.get('status')

        if status == 'added':
            lines.append(f"Property '{current_key}' was added with value: {format_value(value['value'])}")
        elif status == 'removed':
            lines.append(f"Property '{current_key}' was removed")
        elif status == 'changed':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(f"Property '{current_key}' was updated. From {old_value} to {new_value}")
        elif status == 'unchanged' and isinstance(value['value'], dict):
            lines.append(format_plain(value['value'], current_key))

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return '[complex value]'
