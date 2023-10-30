import text

def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:
            print(item)
        else:
            print(f'{item}')

    while True:
        choice = input(text.input_chouce)
        if choice.isdigit() and len(text.main_menu) > int(choice) > 0:
            return int(choice)
        print(text.input_menu_error)

def print_message(msg: str ):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')

def show_notes(notes: dict, msg: str):
    if notes:
        space = ' '
        for i, note in enumerate(notes, 1):
            lst = list(note.values())
            print(f'{i:>4}. {space:<10} {lst[1]:<20} {lst[2]:<20} {lst[3]:<20}')
    else:
        print_message(msg)

def new_note():
    new = []
    for item in text.new_note:
        new.append(input(item))
    return new

def find_note():
    return input(text.find_note)

def edit_note():
    return input(text.edit_note)

def delete_note():
    return input(text.delete_note)