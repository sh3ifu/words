import warnings
warnings.filterwarnings("ignore", message="Your system is avx2 capable")
import io
import pygame
import requests
from colorama import Fore, Style

from config import FILE_PATH
from work_with_files import read_json, save_to_json, read_lines
from words import shuffle_dict, shuffle_list
from keyboards import is_latin, change_keyboard_layout


def __print_add_inform(data):
    print()
    for inf in data:
        print(f'• {inf}')
    print()


def __pronounce(word):
    url = "https://d1qx7pbj0dvboc.cloudfront.net/"
    response = requests.get(url + word + '.mp3')

    if response.status_code == 200:
        audio_data = io.BytesIO(response.content)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_data)
        pygame.mixer.music.set_volume(5)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def learning_mode(learning_mode_commands={}, words=None, category_name='', pronounce=False):
    if (category_name == '') and (words == None):
        while True:
            category_name = input('\nEnter a category name: ')
            if category_name == '!stop':
                return
            else:
                break

    while True:
        correct_answers = 0
        if words == None:
            words = read_json(FILE_PATH)
            if category_name not in words:
                print(Fore.RED + 'Incorrect category name!' + Style.RESET_ALL + '')
                return
            words = shuffle_dict(words, category_name)
        else:
            words = shuffle_dict(words, category_name, all=True)

        mode = input(f'Mode(1, 2 or 3): '); print()

        if mode == '!stop':
            return
        if mode != '1' and mode != '2' and mode != '3':
            print(Fore.RED + 'Incorrect mode!' + Style.RESET_ALL + '')
            continue
        
        mode = int(mode)

        if mode == 1 or mode == 2:
            for word in words:
                word1 = word
                word2 = words[word]['translation']

                if mode == 2:
                    word1, word2 = word2, word1

                if pronounce and mode == 1:
                    __pronounce(word1)

                w = input(f'{word1} - ')

                if w == '!stop':
                    return                
                if w == '!repeat':
                    new_words = read_json(FILE_PATH)

                    new_words['repeat'][word] = words[word]                    
                    save_to_json(FILE_PATH, new_words)
                    
                    print(Fore.YELLOW + 'Word [' + Fore.MAGENTA + word1 + Fore.YELLOW + ' - ' + Fore.CYAN + word2 + Fore.YELLOW + '] successfully added to repeat category!' + Style.RESET_ALL + '\n')
                    continue

                if w == word2:
                    print(Fore.GREEN + 'Correct!\n' + Style.RESET_ALL + '')                    
                    correct_answers += 1
                else:
                    print(Fore.RED + f'Incorrect! Correct answer is: {word2}\n' + Style.RESET_ALL + '')                    
            
            print(Fore.YELLOW + f'Correct answers: {correct_answers} / {len(words)}' + Style.RESET_ALL + '')

        else:
            new_words_list = []

            for word in words:
                word1 = word
                word2 = words[word]['translation']
                new_words_list.append((word1, word2))
                new_words_list.append((word2, word1))
            
            new_words_list = shuffle_list(new_words_list)

            for word in new_words_list:
                latin = False
                word1, word2 = word[0], word[1]

                if is_latin(word1[0]):
                    latin = True
                    change_keyboard_layout(True)
                    if pronounce:
                        __pronounce(word1)
                else:
                    change_keyboard_layout(False)

                w = input(f'{word1} - ')

                if w == '!stop':
                    return                
                if w == '!repeat':
                    new_words = read_json(FILE_PATH)

                    if latin:
                        new_words['repeat'][word1] = words[word1]
                    else:
                        new_words['repeat'][word2] = words[word2]
                    save_to_json(FILE_PATH, new_words)
                    
                    print(Fore.YELLOW + 'Word [' + Fore.MAGENTA + word1 + Fore.YELLOW + ' - ' + Fore.CYAN + word2 + Fore.YELLOW + '] successfully added to repeat category!' + Style.RESET_ALL + '\n')
                    continue

                if w == word2:
                    print(Fore.GREEN + 'Correct!\n' + Style.RESET_ALL + '')
                    correct_answers += 1
                else:
                    print(Fore.RED + f'Incorrect! Correct answer is: {word2}\n' + Style.RESET_ALL + '')                
        
            print(Fore.YELLOW + f'Correct answers: {correct_answers} / {len(words) * 2}' + Style.RESET_ALL + '')

def irregular(*args):
    words = read_lines('words/irregular.txt')
    words = shuffle_list(words)
    
    for word in words:
        word1, word2, word3 = word.split('\t')
        forms = input(f'{word1} - ').split(' ')

        if forms[0] == word2 and forms[1] == word3:
            print(Fore.GREEN + 'Correct!' + Style.RESET_ALL + '')
        else:
            print(Fore.RED + 'Incorrect! Correct forms are: ' + Fore.CYAN + f'{word1}  {word2}  {word3}' + Style.RESET_ALL + '')            
