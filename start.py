import os
import types
from gendiff import generate_diff


file_1 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file1.json')
file_2 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file2.json')


diff = generate_diff(file_1, file_2)
print(diff)
print(isinstance(generate_diff, types.FunctionType))