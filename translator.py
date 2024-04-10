import re
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from translate import Translator


def read_from_file(filename='words/fa16k.txt'):
    file = open(filename, 'r')
    data = file.read()
    file.close()

    return data


def translate_text(text, target='uk'):
    translator = Translator(to_lang=target)
    translation = translator.translate(text)

    return translation

def file_translate(data_string, text):
    lines = data_string.split('\n')
    translations = []
    
    for i, line in enumerate(lines, 1):
        if text in line:
            line = re.sub(r'^.*?\]', '', line)
            translations.append(line)

    return translations

def site1_translate(word):
    translations = []
    url = f'https://www.dict.com/%D0%B0%D0%BD%D0%B3%D0%BB%D1%96%D0%B8%D1%81%D1%8C%D0%BA%D0%BE-%D1%83%D0%BA%D1%80%D0%B0%D1%96%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D0%B8/{word}'
    try:
        response = requests.get(url)
        html_code = response.text

        soup = BeautifulSoup(html_code, 'html.parser')

        tags_with_lex_ful = soup.find_all(class_=lambda value: value and 'lex_ful_tran' in value)

        for tag in tags_with_lex_ful:
            translations.append(tag.text)
    except Exception:
        print(Exception)
    
    return translations

def site2_translate(word):
        try:
            url = f'https://e2u.org.ua/s?w={word}&dicts=all&highlight=on&filter_lines=on'

            response = requests.get(url)
            html_code = response.text

            soup = BeautifulSoup(html_code, 'html.parser')


            td_element = soup.find('td', class_='result_row_main')

            text_without_tags = td_element.get_text(strip=True)

            text_without_tags = re.sub(r'^.*?v', '', text_without_tags)
            text_without_tags = re.sub(r'^.*?\]', '', text_without_tags)
            text_without_tags = text_without_tags.split(';')
        except Exception:
            return []
        
        return text_without_tags

def site3_translate(word):
    url = f'https://uk.glosbe.com/en/uk/{word}'
    try:
        response = requests.get(url)
        html_code = response.text

        soup = BeautifulSoup(html_code, 'html.parser')
    
        p_element = soup.find('p', class_='text-xs')
        strong_element = p_element.find('strong')
        text_without_tags = strong_element.get_text(strip=True)
    except Exception:
        return ''

    return text_without_tags


def translate_word(*args):
    data = read_from_file()
    
    while True:
        print(Fore.MAGENTA + '\n\ntext: ' + Style.RESET_ALL, end='')
        text = input()

        if text == '!stop':
            return
        
        translated_text = translate_text(text)
        file_translations = file_translate(data, text)
        site1_translations = site1_translate(text)
        site2_translations = site2_translate(text)
        site3_translations = site3_translate(text)

        
        print(Fore.CYAN + f'\nTRANSLATOR\n' + Style.RESET_ALL + f'{translated_text}' + Style.RESET_ALL)
        print(Fore.CYAN + f'\nFILE' + Style.RESET_ALL)
        for translation in file_translations:
            print(translation)
        print(Fore.CYAN + f'\nSITE1' + Style.RESET_ALL)
        for translation in site1_translations:
            print(translation)
        print(Fore.CYAN + f'\nSITE3' + Style.RESET_ALL)
        print(site3_translations)
        print(Fore.CYAN + f'\nSITE2' + Style.RESET_ALL)
        for translation in site2_translations:
            print(translation)
