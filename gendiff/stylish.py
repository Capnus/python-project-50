def format_stylish(diff, depth=1):
    result = []
    indent = " " * (depth * 4 - 2)  
    for item in diff:
        key = item["key"]
        type_ = item["type"]
        if type_ == "added":
            result.append(f"{indent}+ {key}: {format_value(item['value'], depth)}")
        elif type_ == "removed":
            result.append(f"{indent}- {key}: {format_value(item['value'], depth)}")
        elif type_ == "unchanged":
            result.append(f"{indent}  {key}: {format_value(item['value'], depth)}")
        elif type_ == "changed":
            result.append(f"{indent}- {key}: {format_value(item['old_value'], depth)}")
            result.append(f"{indent}+ {key}: {format_value(item['new_value'], depth)}")
        elif type_ == "nested":
            children = format_stylish(item["children"], depth + 1)
            result.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")
    return "\n".join(result)


def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        lines = [f"{indent}{k}: {format_value(v, depth + 1)}" for k, v in value.items()]
        return f"{{\n{'\n'.join(lines)}\n{' ' * ((depth - 1) * 4)}}}"  
    if isinstance(value, bool):  
        return str(value).lower()
    if value is None:  
        return "null"
    return str(value)
