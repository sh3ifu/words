from colorama import Fore, Style

from work_with_files import read_json
from config import FILE_PATH
from translator import translate_word


def start_command(*args):
    from words import check_command
    from learning import irregular
    
    commands = {
        'default': launch_learning,
        'all': all,
        'last': last,
        'several': several,
        'translator': translate_word,
        'irregular': irregular,
    }

    check_command(args[0][0], commands, args)


def last(*args):
    from learning import learning_mode
    
    data = read_json(FILE_PATH)
    all_categories = list(data.keys())
    learning_mode(category_name=all_categories[-2])


def all(*args):
    from learning import learning_mode
    
    data = read_json(FILE_PATH)
    categories = list(data.keys())
    categories = categories[:-1]
    all_words = {}

    for category in categories:
        words = list(data[category].keys())
        for word in words:
            all_words[word] = (data[category][word])
    
    learning_mode(words=all_words)


def several(*args):
    from learning import learning_mode
    
    data = read_json(FILE_PATH)
    categories = list(data.keys())
    selected_categories = input('Categories: ')
    selected_categories = selected_categories.split()
    
    for selected_category in selected_categories:
        if selected_category not in categories:
            print(Fore.RED + '\nIncorrect category name!')
            print(Style.RESET_ALL + '') 
            return
    
    words = {}
    for category in selected_categories:
        words.update(data[category])
    
    learning_mode(words=words)


def launch_learning(*args):
    from learning import learning_mode

    try:
        if args[0][0][1:][0] == '!pr':
            learning_mode(pronounce=True)
    except Exception:
        learning_mode()
