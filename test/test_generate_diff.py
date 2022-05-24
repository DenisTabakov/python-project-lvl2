from gendiff import generate_diff


def test_generate_diff(file_1, file_2):
    assert generate_diff(file_1, file_2) == \
           '{' \
           '- follow: False host: hexlet.io ' \
           '- proxy: 123.234.53.22 ' \
           '- timeout: 50 ' \
           '+ timeout: 20 ' \
           '+ verbose: True' \
           '}'
