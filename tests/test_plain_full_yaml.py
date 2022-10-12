from engine.generate_diff import get_diff
from formaters.plain import convert
import os
import yaml
from yaml.loader import SafeLoader


file_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s1.yaml')
file_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s2.yaml')
file_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_plain_full.txt')

with open(file_1) as f_1:
    data_1 = yaml.load(f_1, Loader=SafeLoader)

with open(file_2) as f_2:
    data_2 = yaml.load(f_2, Loader=SafeLoader)

with open(file_3) as f_3:
    ref_diff = f_3.read()


def test_stylish_full():
    assert convert(get_diff(data_1, data_2)) == ref_diff