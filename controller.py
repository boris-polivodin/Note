import time

import text
import view
import  model

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.file_load_successful)
            case 2:
                notes = model.notes
                view.show_notes(notes, text.empty_notes)
            case 3:
                search = view.find_note()
                result = model.find_note(search)
                view.show_notes(result, text.empty_notes)
            case 4:
                new_data = view.new_note()
                new_data.insert(0, str(len(model.notes)))
                new_data.append(time.asctime(time.localtime(time.time())))
                model.add_note(new_data)
                view.print_message(text.note_save_successful(new_data[1]))
            case 5:
                search = view.find_note()
                result = model.find_note(search)
                view.show_notes(result, text.empty_notes)
                if len(result) > 0:
                    responce = view.edit_note()
                    if responce == 'д' or responce == 'y':
                        new_data = view.new_note()
                        notes = model.notes
                        for note_search in result:
                            for note in notes:
                                if note['id'] == note_search['id']:
                                    if new_data[0] != '':
                                        note['title'] = new_data[0]
                                    if new_data[1] != '':
                                        note['body'] = new_data[1]
                                    view.print_message(text.note_save_successful(note['title']))
                                    break
                        model.save_file()
            case 6:
                search = view.find_note()
                result = model.find_note(search)
                view.show_notes(result, text.empty_notes)
                if len(result) > 0:
                    responce = view.delete_note()
                    if responce == 'д' or responce == 'y':
                        notes = model.notes
                        for note_search in result:
                            title = note_search['title']
                            notes.remove(note_search)
                            view.print_message(text.note_delete_successful(title))
                        model.save_file()
            case 7:
                view.print_message(text.end_program)
                break



