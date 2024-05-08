import os
from colorama import Fore, Style

from config import FILE_PATH
from work_with_files import read_json, save_to_json
from keyboards import change_keyboard_layout


def __split_string(string):
    split_string = string.split('\t')

    if len(split_string) == 1 and split_string[0] == '':
        return []
    
    return split_string

def add_command(*args):
    from words import check_command
    
    commands = {
        'category': add_category,
        'word': add_word,
        'words': add_words,
    }

    check_command(args[0][0], commands, args)


def add_category(*args):
    category_name = input('Category name: ')
        
    if category_name == 'stop':
        return
    
    data = read_json(FILE_PATH)
    
    if category_name in data:
        print(Fore.RED + '\nCategory already exists!' + Style.RESET_ALL + '')
        return
    
    data[category_name] = {}
    data["repeat"] = data.pop("repeat")
    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nCategory successfully added!' + Style.RESET_ALL + '')


def add_word(*args):
    category_name = input('Category name: ')
    
    if category_name == 'stop':
        return
    
    data = read_json(FILE_PATH)
    
    if not category_name in data:
        print(Fore.RED + '\nIncorrect category name!')
        print(Style.RESET_ALL + '')
        return
    
    change_keyboard_layout(False)
    word = input('\nWord: '); change_keyboard_layout(True)
    translation = input('Translation: ')
    additional_translations = input('Additional translations: ')
    associations = input('Associations: ')
    sentences = input('Sentences: ')

    additional_translations = __split_string(additional_translations)
    associations = __split_string(associations)
    sentences = __split_string(sentences)

    if word == 'stop' or translation == 'stop' or additional_translations == 'stop' or associations == 'stop' or sentences == 'stop':
        print(Fore.YELLOW + '\nAddition of new words has stopped!')
        print(Style.RESET_ALL + '')
        return
    
    data[category_name].update({word: {"translation": translation, "additional translations": additional_translations, "associations": associations, "sentences": sentences}})
    save_to_json(FILE_PATH, data)

    print(Fore.GREEN + '\nWord successfully added!')
    print(Style.RESET_ALL + '')


def add_words(*args):
    category_name = input('Category name: ')
    
    if category_name == 'stop':
        return
    
    data = read_json(FILE_PATH)
    
    if not category_name in data:
        print(Fore.RED + '\nIncorrect category name!')
        print(Style.RESET_ALL + '')
        return
    
    words_count = int(input('Enter words count: '))
    for i in range(words_count):
        change_keyboard_layout(False)
        word = input(f'\n{i+1}.  Word: '); change_keyboard_layout(True)    
        translation = input('Translation: ')
        additional_translations = input('Additional translations: ')
        associations = input('Associations: ')
        sentences = input('Sentences: ')

        additional_translations = __split_string(additional_translations)
        associations = __split_string(associations)
        sentences = __split_string(sentences)

        if word == '!stop' or translation == '!stop' or additional_translations == '!stop' or associations == '!stop' or sentences == '!stop':
            print(Fore.YELLOW + '\nAddition of new words has stopped!' + Style.RESET_ALL + '')
            return

        data[category_name].update({word: {"translation": translation, "additional translations": additional_translations, "associations": associations, "sentences": sentences}})
        save_to_json(FILE_PATH, data)

        print(Fore.GREEN + '\nWord successfully added!' + Style.RESET_ALL + '')


def find(*args):
    find_word = args[0]

    data = read_json(FILE_PATH)
    categories = list(data.keys())
    categories = categories[:-1]
    all_words = {}

    for category in categories:
        words = list(data[category].keys())

        for word in words:
            all_words[word] = (data[category][word])
    
    if find_word[0] in all_words:
        print(Fore.YELLOW+ 'Yes' + Style.RESET_ALL)
        print(find_word[0], '-', all_words[find_word[0]]['translation'])
    else:
        print(Fore.RED+ 'No' + Style.RESET_ALL)
