import json


def convert(data):
    return json.dumps(format_(data), indent=3)


def format_(data):
    result = {}

    def check_data(*args):
        for item in args:
            member, value = item
            if member == "children":
                args = format_(value)
        return args
    for item in data.keys():
        flag, key = item
        if flag == "changed":
            old, new = check_data(data[item][0], data[item][1])
            value = ["updated", old, new]
        else:
            if flag == "no change":
                value = check_data(data[item])
            else:
                value = [flag, check_data(data[item])]
        result[key] = value
    return result
