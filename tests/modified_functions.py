from gendiff.formaters.stylish import format_, edit_word


def convert_t(data):
    return edit_word(stringify_t(format_(data)))


def stringify_t(data, spaces_count=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = stringify_t(value, spaces_count + 1)
        preform = f"{'    ' * spaces_count}{key}: {value}"
        result += f"{preform.rstrip()}\n"
    result += f"{'    ' * spaces_count}}}"
    return result
