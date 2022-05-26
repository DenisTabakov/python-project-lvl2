from gendiff.generate_diff import gen_diff


def test_generate_diff():
    file_1 = 'file1.json'
    file_2 = 'file2.json'
    assert gen_diff(file_1, file_2) == \
           '{\n' \
           ' - follow: False\n' \
           '   host: hexlet.io\n' \
           ' - proxy: 123.234.53.22\n' \
           ' - timeout: 50\n' \
           ' + timeout: 20\n' \
           ' + verbose: True\n' \
           '}'
