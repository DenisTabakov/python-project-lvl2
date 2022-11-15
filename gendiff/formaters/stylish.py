CONDITION = {
    "added": "  + ",
    "removed": "  - ",
    "no change": "    "
}


def convert(data):
    return edit_word(stringify(format_(data)))


def transform(data):
    if not isinstance(data, dict):
        return data

    result = {}
    for key, value in data.items():
        new_key = '    {}'.format(key)
        result[new_key] = transform(value)
    return result


def format_(data):

    result = {}
    for flag_key, main_data in data.items():
        flag, key = flag_key
        member, value = main_data
        if member == 'children':
            result[CONDITION[flag] + key] = format_(value)
        elif flag == "changed":
            old_value_type, old_value = main_data[0]
            new_value_type, new_value = main_data[1]
            result[CONDITION["removed"] + key] = transform(old_value)
            result[CONDITION["added"] + key] = transform(new_value)
        else:
            result[CONDITION[flag] + key] = transform(value)
    return result


def stringify(data, spaces_count=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = stringify(value, spaces_count + 1)
        result += f"{'    ' * spaces_count}{key}: {value}\n"
    result += f"{'    ' * spaces_count}}}"
    return result


def edit_word(word):
    if "False" in word:
        word = word.replace("False", "false")
    if "True" in word:
        word = word.replace("True", "true")
    if "None" in word:
        word = word.replace("None", "null")
    return word
