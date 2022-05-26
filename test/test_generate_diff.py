from gendiff import generate_diff


def test_generate_diff(file_1, file_2):
    assert generate_diff(file_1, file_2) == \
           '{\n' \
           '- follow: False host: hexlet.io\n' \
           '- proxy: 123.234.53.22\n' \
           '- timeout: 50\n' \
           '+ timeout: 20\n' \
           '+ verbose: True\n' \
           '}'
