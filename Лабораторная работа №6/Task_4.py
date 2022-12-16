import json

INPUT_FILE = "input.csv"


def line_separ(line_s, delimeter=',') -> list:
    line_s = line_s.rstrip()
    line_s = line_s.split(delimeter)
    return line_s


def csv_to_list_dict(filename) -> list[dict]:
    with open(INPUT_FILE, 'r') as f:

        json_list = []
        keys = line_separ(f.readline())

        for lines in f:
            lines_new = line_separ(lines)
            json_list.append(dict(zip(keys, lines_new)))

    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


