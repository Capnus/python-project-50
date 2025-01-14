INDENT_SIZE = 4
INDENT_OFFSET = 2


def walk(node, depth):

    space = " " * (INDENT_SIZE * depth - INDENT_OFFSET)  
    lines = []

    if not isinstance(node, dict):
        return format_value(node)  

    for key, value in node.items():
        if isinstance(value, dict) and "status" in value:
            status = value.get("status")
            if status == "added":
                lines.append(
                    f"{space}+ {key}: {walk(value['value'], depth + 1)}"
                )
            elif status == "removed":
                lines.append(
                    f"{space}- {key}: {walk(value['value'], depth + 1)}"
                )
            elif status == "unchanged":
                lines.append(
                    f"{space}  {key}: {walk(value['value'], depth + 1)}"
                )
            elif status == "changed":
                lines.append(
                    f"{space}- {key}: {walk(value['old_value'], depth + 1)}"
                )
                lines.append(
                    f"{space}+ {key}: {walk(value['new_value'], depth + 1)}"
                )
        else:
            lines.append(f"{space}  {key}: {walk(value, depth + 1)}")

    closing_indent = (INDENT_SIZE * (depth - 1))
    result = "{\n" + "\n".join(lines) + "\n" + " " * closing_indent + "}"
    return result


def format_value(value):
    if isinstance(value, dict):
        return walk(value, 1)  
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_stylish(diff):
    return walk(diff, 1)  
