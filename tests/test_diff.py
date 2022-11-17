from gendiff.generate_diff import get_diff
from tests.modified_functions import convert_t
from gendiff.generate_diff import generate_diff
from gendiff.parser import parse
import os


json_small_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file1.json')
json_small_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file2.json')
json_full_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full1.json')
json_full_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full2.json')
yaml_full_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full1.yaml')
yaml_full_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full2.yaml')
yml_full_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full1.yml')
yml_full_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_full2.yml')
out_stylish_small = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_stylish.txt')
out_stylish_full = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_stylish_full.txt')
out_plain_full = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_plain_full.txt')
out_json_full = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_json_full.txt')

data_json_full_1 = parse(json_full_1)
data_json_full_2 = parse(json_full_2)
data_yaml_full_1 = parse(yaml_full_1)
data_yaml_full_2 = parse(yaml_full_2)
data_yml_full_1 = parse(yml_full_1)
data_yml_full_2 = parse(yml_full_2)
diff_stylish_small = parse(out_stylish_small)
diff_stylish_full = parse(out_stylish_full)
diff_plain_full = parse(out_plain_full)
diff_json_full = parse(out_json_full)


def test_parse():
    assert data_json_full_1 == data_yaml_full_1
    assert data_json_full_2 == data_yaml_full_2
    assert data_json_full_1 == data_yml_full_1
    assert data_json_full_2 == data_yml_full_2


def test_stylish():
    assert generate_diff(json_small_1, json_small_2) == diff_stylish_small
    assert convert_t(get_diff(data_json_full_1, data_json_full_2)) == diff_stylish_full


def test_plain():
    assert generate_diff(json_full_1, json_full_2, output_format='plain') == diff_plain_full


def test_json():
    assert generate_diff(json_full_1, json_full_2, output_format='json') == diff_json_full
