import json


def read_from_file(filename, mode='r'):
    file = open(filename, mode, encoding='utf-8')
    data = file.read()
    file.close()

    return data

def read_lines(filename):
    lines = []
    file = open(filename, 'r')    

    for line in file:
        line = line.strip()
        
        lines.append(line)

    file.close()

    return lines

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

def save_to_json(filename, data):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
