from engine.generate_diff import get_diff
from formaters.plain import convert
import os
import json


file_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file1.json')
file_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file2.json')
file_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file_plan.txt')

with open(file_1) as json_file_1:
    data_1 = json.load(json_file_1)

with open(file_2) as json_file_2:
    data_2 = json.load(json_file_2)

with open(file_3) as file_plan:
    ref_diff = file_plan.read()


def test_plan():
    assert convert(get_diff(data_1, data_2)) == ref_diff