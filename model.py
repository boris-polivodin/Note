import controller


class Notebook:

    def __init__(self, path: str = 'note.txt'):
        self.notes = []
        self.path = path

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for i, note in enumerate(data, 1):
                note = note.strip().split(';')
                # notes.append(note)
                self.notes.append({'id': note[0], 'title': note[1], 'body': note[2], 'timestamp': note[3]})

    def save_file(self):
        result = []
        for note in self.notes:
            line = ';'.join(note.values())
            result.append(line)
        result = '\n'.join(result)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(result)

    def add_note(self, new: list[str]):
        self.notes.append({'id': new[0], 'title': new[1], 'body': new[2], 'timestamp': new[3]})
        self.save_file()

    def find_note(self, line: str):
        result = []
        for note in self.notes:
            for field in note.values():
                if line.lower() in field.lower():
                    result.append(note)
                    break
        return result

    def edit_notes(self, result: []):
        new_data = controller.new_note()
        for note_search in result:
            for note in self.notes:
                if note['id'] == note_search['id']:
                    if new_data[0] != '':
                        note['title'] = new_data[0]
                    if new_data[1] != '':
                        note['body'] = new_data[1]
                    controller.print_note_save_successful(note['title'])
                    break
        self.save_file()

    def delete_notes(self,result: []):
        for note_search in result:
            title = note_search['title']
            self.notes.remove(note_search)
            controller.print_note_delete_successful(title)
        self.save_file()
