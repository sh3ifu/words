import os
import random

from practice import practice
from commands.menu_commands import *
from commands.add_commands import add_command, find
from commands.launch_commands import start_command
from commands.list_commands import list_command
from commands.count_commands import count_command
from commands.delete_commands import delete_command


def shuffle_dict(input_dict, category_name, all=False):
    if not all:
        keys = list(input_dict[category_name].keys())
    else:
        keys = list(input_dict.keys())

    for _ in range(5):
        random.shuffle(keys)

    if not all:
        shuffled_data = {key: input_dict[category_name][key] for key in keys}
    else:
        shuffled_data = {key: input_dict[key] for key in keys}

    return shuffled_data

def shuffle_list(input_list):
    for _ in range(5):
        random.shuffle(input_list)
    
    return input_list


def command_parse(command):
    commands = command.split()
    return commands

def check_command(command, commands, *args):    
    if command in commands:
        commands[command](*args)
    else:
        print('Command does not exist.')    


def main(menu_commands, learning_mode_commands):
    while True:
        command = input('\n> ')

        command = command_parse(command)        
        check_command(command[0], menu_commands, command[1:])


if __name__ == '__main__':
    clear()
    
    menu_commands = {
        "start": start_command,
        "practice": practice,
        "list": list_command,
        "add": add_command,
        "delete": delete_command,
        "count": count_command,
        "merge": merge,
        "clear": clear,
        "clean": clean,
        "find": find,
        "help": help,
        "exit": exit,
    }

    learning_mode_commands = {
        "stop": "",
    }
    
    main(menu_commands, learning_mode_commands)
