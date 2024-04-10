from colorama import Fore, Style

from work_with_files import *
from config import FILE_PATH


def list_command(*args):
    from words import check_command
    
    commands = {
        'words': list_words,
        'categories': list_categories,
    }

    check_command(args[0][0], commands, args)


def __print_add_info(info_name, text):
    if len(text) == 0:
        return
    
    print(Fore.YELLOW + info_name)
    for t in text:
        print(Fore.CYAN + f'  • {t}')
    print(Style.RESET_ALL + '', end='')


def list_words(*args):
    args = args[0][0][1:]
    flag = False
    category_name = input('Category name: ')    
    data = read_json(FILE_PATH)
    if category_name not in data:
        print(Fore.RED + 'Incorrect category name!' + Style.RESET_ALL + '')
        return
    words = data[category_name]

    print()
    for word in words:
        print(f'{word.ljust(11)} - {words[word]["translation"]}')

        if '!at' in args:
            __print_add_info('translations: ', words[word]['additional translations'])
            flag = True
        if '!a' in args:
            __print_add_info('associations: ', words[word]['associations'])
            flag = True
        if '!s' in args:
            __print_add_info('sentences: ', words[word]['sentences'])
            flag = True
        if '!all' in args:
            __print_add_info('translations: ', words[word]['additional translations'])
            __print_add_info('associations: ', words[word]['associations'])
            __print_add_info('sentences: ', words[word]['sentences'])
            flag = True
        if flag:
            print('\n')
    
    print(f'\nTotal count: {len(words)}')


def list_categories(*args):
    data = read_json(FILE_PATH)
    categories = list(data.keys())
    
    print()
    for category in categories:
        print(category)
    
    print(f'\nTotal count: {len(categories)}')
