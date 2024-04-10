import os
import sys
from colorama import Fore, Style

from work_with_files import read_from_file, read_json, save_to_json
from config import HELP_PATH, FILE_PATH


def exit(*args):
    sys.exit()

def clear(*args):
    os.system('cls' if os.name == 'nt' else 'clear')

def help(*args):
    print(read_from_file(HELP_PATH))

def clean(*args):
    try:
        category_name = args[0][0]
    except Exception:
        print(Fore.RED + '\nIncorrect arguments!' + Style.RESET_ALL + '')
        return
    
    data = read_json(FILE_PATH)

    if not category_name in data:
        print(Fore.RED + '\nIncorrect category name!' + Style.RESET_ALL + '')
        return
    
    data[category_name] = {}
    
    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nCategory successfully cleaned!' + Style.RESET_ALL + '')
    

def merge(*args):
    categories = input('Categories: ')
    new_category_name = input('New category name: ')
    
    categories = categories.split(' ')
    data = read_json(FILE_PATH)
    categories_data = {}

    for category in categories:
        if not category in data:
            print(category + Fore.RED + '\nIncorrect category name!' + Style.RESET_ALL + '')
            return
        categories_data.update(data[category])
    
    if new_category_name in data:
        print('\n' + Fore.YELLOW + 'Category already exist. Are you sure you want to continue?' + Style.RESET_ALL + '')
        answer = input('Y or N: ').lower()
        if answer == 'n' or answer == 'no':
            return
    
    for category in categories:
        del data[category]
    
    data[new_category_name] = categories_data
    data["repeat"] = data.pop("repeat")
    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nCategories successfully merged!' + Style.RESET_ALL + '')
