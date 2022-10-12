def convert(data):
    return edit_word(get_string(format_(data)))


def format_(data, spacer=""):
    result = []
    for item in data.keys():
        flag = item[0]
        key = spacer + item[1]
        if flag == "added":
            value = transform(data[item][1])
            result.append(f"Property '{key}' was added with value: {value}")
        elif flag == "removed":
            result.append(f"Property '{key}' was removed")
        elif flag == "changed":
            old_value = transform(data[item][0][1])
            new_value = transform(data[item][1][1])
            result.append(
                f"Property '{key}' was updated. From {old_value} to {new_value}"
            )
        else:
            member, value = data[item]
            if member == "children":
                result.extend(format_(value, key + "."))
    return result


def transform(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return value


def get_string(data):
    return "\n".join(data)


def edit_word(word):
    if "False" in word:
        word = word.replace("False", "false")
    if "True" in word:
        word = word.replace("True", "true")
    if "None" in word:
        word = word.replace("None", "null")
    return word
