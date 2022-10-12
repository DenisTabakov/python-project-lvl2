import os
from gendiff.formaters import j_son, plain
from gendiff.formaters import stylish
from gendiff.parser import choose_format

OUT_FORMATS = {'stylish': stylish.convert, 'plain': plain.convert, 'json': j_son.convert}


def generate_diff():
    data_1, data_2, output_format, output_extension = choose_format()
    result = OUT_FORMATS[output_format](get_diff(data_1, data_2))

    if output_extension != "None":
        path_1 = os.path.join(os.getcwd(), 'output.')
        output_path = f"{path_1}{str(output_extension)}"
        with open(output_path, "w") as output_file:
            output_file.write(result)

    return result


def get_diff(data_1, data_2):
    result = {}
    keys = sorted(data_1.keys() | data_2.keys())
    for key in keys:
        val_1, val_2 = data_1.get(key), data_2.get(key)
        if key in data_1 and key not in data_2:
            flag = "removed"
            value = ["value", val_1]
        elif key in data_2 and key not in data_1:
            flag = "added"
            value = ["value", val_2]
        elif val_1 == val_2:
            flag = "no change"
            value = ["value", val_1]
        elif isinstance(val_1, dict) and isinstance(val_2, dict):
            flag = "no change"
            value = ["children", get_diff(val_1, val_2)]
        else:
            flag = "changed"
            value = [["value", val_1], ["value", val_2]]
        result[flag, key] = value
    return result

