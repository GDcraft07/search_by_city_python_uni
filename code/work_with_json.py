import json

def read_json(file: str) -> dict:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def add_to_json(file: str, data_to_add: tuple) -> bool:
    data = read_json(file)

    if data_to_add[0] in data.keys():
        return False

    data[data_to_add[0]] = data_to_add[1]

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    return True


def edit_json(file: str, data_to_edit: tuple) -> bool:
    data = read_json(file)

    if data_to_edit[0] not in data.keys():
        return False

    data[data_to_edit[0]] = data_to_edit[1]

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return True


def delet_json(file: str, data_to_delet: str) -> bool:
    data = read_json(file)

    if data_to_delet not in data.keys():
        return False

    data.pop(data_to_delet)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return True
