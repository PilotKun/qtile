import os
import random
from libqtile import qtile, hook
from typing import Callable

from settings import WALLPAPERS_PATH, WALLPAPER_TIMEOUT_MINUTES

class Timer():
    def __init__(self, timeout: int, callback: Callable) -> None:
        self.callback = callback
        self.timeout = timeout
        self.call()

    def call(self) -> None:
        self.callback()
        self.setup_timer()

    def setup_timer(self) -> None:
        self.timer = qtile.call_later(self.timeout, self.call)


def set_random_wallpaper() -> None:
    valid_exts = (".jpg", ".jpeg", ".png")
    wallpapers = [
        os.path.join(WALLPAPERS_PATH, x) 
        for x in os.listdir(WALLPAPERS_PATH) 
        if x.lower().endswith(valid_exts)
    ]
    
    if not wallpapers:
        return

    wallpaper = random.choice(wallpapers)
    set_wallpaper(wallpaper)


def set_wallpaper(file_path: str) -> None:
    for screen in qtile.screens:
        screen.cmd_set_wallpaper(file_path, 'fill')

@hook.subscribe.startup_once
def setup_wallpaper_timer():
    Timer(WALLPAPER_TIMEOUT_MINUTES * 60, set_random_wallpaper)
