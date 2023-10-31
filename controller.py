import time

import text
import view
from model import Notebook


def start():
    nb = Notebook()
    while True:
        choice = view.menu()
        match choice:
            case 1:
                nb.open_file()
                view.print_message(text.file_load_successful)
            case 2:
                notes = nb.notes
                view.show_notes(notes, text.empty_notes)
            case 3:
                search = view.find_note()
                result = nb.find_note(search)
                view.show_notes(result, text.empty_notes)
            case 4:
                new_data = view.new_note()
                new_data.insert(0, str(len(nb.notes)))
                new_data.append(time.asctime(time.localtime(time.time())))
                nb.add_note(new_data)
                view.print_message(text.note_save_successful(new_data[1]))
            case 5:
                search = view.find_note()
                result = nb.find_note(search)
                view.show_notes(result, text.empty_notes)
                if len(result) > 0:
                    responce = view.edit_note()
                    if responce == 'д' or responce == 'y':
                        nb.edit_notes(result)
            case 6:
                search = view.find_note()
                result = nb.find_note(search)
                view.show_notes(result, text.empty_notes)
                if len(result) > 0:
                    responce = view.delete_note()
                    if responce == 'д' or responce == 'y':
                        nb.delete_notes(result)
            case 7:
                view.print_message(text.end_program)
                break


def new_note():
    return view.new_note()


def print_note_save_successful(title: str):
    view.print_message(text.note_save_successful(title))


def print_note_delete_successful(title: str):
    view.print_message(text.note_delete_successful(title))
