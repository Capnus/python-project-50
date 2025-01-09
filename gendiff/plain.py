def format_plain(diff):


    def inner_format(diff, path=""):
        lines = []
        for item in diff:
            key = item["key"]
            full_path = f"{path}.{key}" if path else key
            diff_type = item["type"]

            if diff_type == "added":
                value = format_value_plain(item["value"])
                lines.append(
                    f"Property '{full_path}' was added with value: {value}"
                )
            elif diff_type == "removed":
                lines.append(f"Property '{full_path}' was removed")
            elif diff_type == "changed":
                old_value = format_value_plain(item["old_value"])
                new_value = format_value_plain(item["new_value"])
                lines.append(
                    f"Property '{full_path}' was updated. "
                    f"From {old_value} to {new_value}"
                )
            elif diff_type == "nested":
                lines.append(inner_format(item["children"], full_path))

        return "\n".join(lines)

    return inner_format(diff)


def format_value_plain(value):
    if isinstance(value, (dict, list, tuple)):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
