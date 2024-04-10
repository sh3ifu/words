from work_with_files import *
from config import FILE_PATH


def count_command(*args):
    from words import check_command
    
    commands = {
        'words': words_count,
        'categories': categories_count,
    }

    check_command(args[0][0], commands, args)
  

def words_count(*args):
    category_name = input('Category name: ')
    data = read_json(FILE_PATH)
    words = data[category_name]

    print(f'\nWords count: {len(words)}')


def categories_count(*args):
    data = read_json(FILE_PATH)
    categories = list(data.keys())
    
    print(f'\nCategories count: {len(categories)}')
