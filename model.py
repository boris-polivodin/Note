notes = []
PATH = 'note.txt'

def open_file():
    global notes
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for i, note in enumerate(data, 1):
            note = note.strip().split(';')
            # notes.append(note)
            notes.append({'id': note[0], 'title': note[1], 'body': note[2], 'timestamp': note[3]})

def save_file():
    global notes
    result = []
    for note in notes:
        line = ';'.join(note.values())
        result.append(line)
    result = '\n'.join(result)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(result)

def add_note(new: list[str]):
    global notes
    notes.append({'id': new[0], 'title': new[1], 'body': new[2], 'timestamp': new[3]})
    save_file()

def find_note(line: str):
    global notes
    result = []
    for note in notes:
        for field in note.values():
            if line.lower() in field.lower():
                result.append(note)
                break
    return result