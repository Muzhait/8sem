import functions
from interface import interface

mode = 0
while mode != 6:
    mode = interface()
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.edit_data()
    elif mode == 5:
        functions.del_data()
    else:
        print("Работа в справочнике заверщена!")
    break