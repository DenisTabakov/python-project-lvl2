from gendiff.generate_diff import get_diff
from gendiff.formaters import stylish, j_son, plain
from gendiff.parser import parse
import os


file_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file1.json')
file_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file2.json')
file_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s1.json')
file_4 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s2.json')
file_5 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s1.yaml')
file_6 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s2.yaml')
file_7 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_stylish.txt')
file_8 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_stylish_full.txt')
file_9 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_plain_full.txt')
file_10 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_json_full.txt')

data_1 = parse(file_1)
data_2 = parse(file_2)
data_3 = parse(file_3)
data_4 = parse(file_4)
data_5 = parse(file_5)
data_6 = parse(file_6)
diff_stylish_small = parse(file_7)
diff_stylish_full = parse(file_8)
diff_plain_full = parse(file_9)
diff_json_full = parse(file_10)


def test_parse():
    assert data_3 == data_5


def test_stylish():
    assert stylish.convert(get_diff(data_1, data_2)) == diff_stylish_small
    assert stylish.convert(get_diff(data_3, data_4)) == diff_stylish_full


def test_plain():
    assert plain.convert(get_diff(data_3, data_4)) == diff_plain_full


def test_json():
    assert j_son.convert(get_diff(data_3, data_4)) == diff_json_full
