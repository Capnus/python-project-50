def format_plain(diff, path=""):
    lines = []

    for item in diff:
        key = item["key"]
        full_path = f"{path}.{key}" if path else key
        type_ = item["type"]

        if type_ == "added":
            value = format_value_plain(item["value"])
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
                )
        elif type_ == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif type_ == "changed":
            old_value = format_value_plain(item["old_value"])
            new_value = format_value_plain(item["new_value"])
            lines.append(
                f"Property '{full_path}' was updated. "
                f"From {old_value} to {new_value}"
                )
        elif type_ == "nested":
            lines.append(format_plain(item["children"], full_path))

    return "\n".join(lines)


def format_value_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)