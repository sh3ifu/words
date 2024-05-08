from work_with_files import read_json, save_to_json
from config import FILE_PATH
from colorama import Fore, Style


def delete_command(*args):
    from words import check_command
    
    commands = {
        'category': delete_category,
        'word': delete_word,
        'words': delete_words,
    }

    check_command(args[0][0], commands, args)


def delete_category(*args):
    category_name = input('Category name: ')
    
    if category_name == '!stop':
        return
    
    data = read_json(FILE_PATH)
    
    if not category_name in data:
        print(Fore.RED + '\nIncorrect category name!' + Style.RESET_ALL + '')
        return

    del data[category_name]

    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nCategory deleted successfully!' + Style.RESET_ALL + '')


def delete_word(*args):
    category_name = input('Category name: ')
    
    if category_name == 'stop':
        return
    
    data = read_json(FILE_PATH)    
    word = input('\nWord: ')

    if (not category_name in data) or (not word in data[category_name]):
        print(Fore.RED + '\nIncorrect input!')
        print(Style.RESET_ALL + '')
        return

    del data[category_name][word]

    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nWord deleted successfully!')
    print(Style.RESET_ALL + '')


def delete_words(*args):
    category_name = input('Category name: '); print()
    
    if category_name == 'stop':
        return
    
    data = read_json(FILE_PATH)

    if not category_name in data:
        print(Fore.RED + '\nIncorrect category name!')
        print(Style.RESET_ALL + '')
        return

    word = ''
    while word != 'stop':
        word = input('Word: ')

        if not word in data[category_name]:
            print(Fore.RED + '\nIncorrect word!')
            print(Style.RESET_ALL + '')
            return

        del data[category_name][word]

        save_to_json(FILE_PATH, data)

        print(Fore.GREEN + '\nWord deleted successfully!')
        print(Style.RESET_ALL + '')
