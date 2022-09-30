from engine.generate_diff import get_diff
from formaters.stylish import convert
import os
import json


file_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s1.yaml')
file_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_s2.yaml')
file_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_stylish_full.txt')

with open(file_1) as f_1:
    data_1 = json.load(f_1)

with open(file_2) as f_2:
    data_2 = json.load(f_2)

with open(file_3) as f_3:
    ref_diff = f_3.read()


def test_stylish_full():
    assert convert(get_diff(data_1, data_2)) == ref_diff
