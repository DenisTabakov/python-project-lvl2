from gendiff.parser import parse
from gendiff.generate_diff import get_diff
from gendiff.formaters import stylish


def generate_diff(file_1, file_2):
    data_1 = parse(file_1)
    data_2 = parse(file_2)
    result = stylish.convert(get_diff(data_1, data_2))
    return result

