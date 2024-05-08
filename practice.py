import os
from colorama import Fore, Style

from config import FILE_PATH
from work_with_files import read_json
from keyboards import change_keyboard_layout

def __print_add_info(info_name, text):
    if len(text) == 0:
        return
    
    print(Fore.YELLOW + info_name)
    for t in text:
        print(Fore.CYAN + f'  • {t}')
    print(Style.RESET_ALL + '', end='')


def practice(*args):
    data = read_json(FILE_PATH)
    category_name = input('Enter category: ')
    words = data[category_name]

    for word in words:
        print(Style.RESET_ALL)
        print(f"\n{word}  -  {words[word]['translation']}")
        __print_add_info('translations: ', words[word]['additional translations'])
        __print_add_info('associations: ', words[word]['associations'])
        __print_add_info('sentences: ', words[word]['sentences'])
        print()

        flag = False
        for i in range(30):
            if i % 3 == 0:
                flag = not flag
            if flag:
                change_keyboard_layout(True)
                input(Fore.MAGENTA + f'{word} - ' + Fore.YELLOW)
            else:
                change_keyboard_layout(False)
                input(Fore.YELLOW+ f"{words[word]['translation']} - " + Fore.MAGENTA)
        print(Style.RESET_ALL)
