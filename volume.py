import os


import pyautogui as pag


def volume_plus(vlm=5):
    cmd = f"amixer -D pulse sset Master {vlm}%+"

    returned_value = os.system(cmd)
    print('returned value:', returned_value)


def volume_minus(vlm=5):
    cmd = f"amixer -D pulse sset Master {vlm}%-"

    returned_value = os.system(cmd)
    print('returned value:', returned_value)


def volume_set(vlm):
    cmd = f"mixer -D pulse sset Master {vlm}%"

    returned_value = os.system(cmd)
    print('returned value:', returned_value)


def google_start(url):
    cmd = f"google-chrome-stable {url}&"

    returned_value = os.system(cmd)
    print('returned value:', returned_value)


def yt_fullscreen():
    pag.hotkey('f')


def yt_pause():
    pag.hotkey('space')


def google_clstr():
    pag.hotkey('ctrl', 'w')
