import os
import ctypes
import pyautogui
from xkbgroup import XKeyboard


def switch_keyboard_layout():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('alt')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('alt')


# ------ LINUX
def get_current_keyboard_layout_linux():
    try:
        keyboard = XKeyboard()
        layout = keyboard.group_name
        return layout
    except Exception as e:
        print("Error getting keyboard layout:", e)
        return None


# ------ WINDOWS
def is_latin(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def get_current_keyboard_layout():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    thread_id = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, 0)
    klid = ctypes.windll.user32.GetKeyboardLayout(thread_id)

    return klid & 0xFFFF

def change_keyboard_layout(latin):
    if latin:
        if os.name == 'np':
            while get_current_keyboard_layout() != 1058:
                switch_keyboard_layout()            
        else:
            while get_current_keyboard_layout_linux() != 'Ukrainian':
                switch_keyboard_layout()
    else:
        if os.name == 'np':
            while get_current_keyboard_layout() != 1033:
                switch_keyboard_layout()
        else:
            while get_current_keyboard_layout_linux() != 'English (US)':
                switch_keyboard_layout()
