from libqtile import bar, extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
import os
import subprocess

# init settings
from settings import mod, terminal, commands, USER_HOME, volume_step, brightness_step, font_family, font_size, font_prompt, font_prompt_size, WALLPAPERS_PATH
# init keybindings
from key_conf import keys, mouse
# init wallpaper
import wallpaper 
extension_defaults = widget_defaults.copy()

sep = widget.Sep(linewidth=1, padding=8, foreground=colors[9])

screens = [
    Screen(
        bottom=bar.Bar(
            widgets = [
                widget.Spacer(length = 8),
                widget.Prompt(
                    font = font_prompt,
                    fontsize=font_size,
                    foreground = colors[1]
                ),
                widget.GroupBox(
                    fontsize = 14,
                    margin_y = 5,
                    margin_x = 5,
                    padding_y = 0,
                    padding_x = 2,
                    borderwidth = 3,
                    active = colors[8],
                    inactive = colors[9],
                    rounded = False,
                    highlight_color = colors[0],
                    highlight_method = "line",
                    this_current_screen_border = colors[7],
                    this_screen_border = colors [4],
                    other_current_screen_border = colors[7],
                    other_screen_border = colors[4],
                ),
                widget.TextBox(
                    text = '|',
                    font = "JetBrainsMono Nerd Font Propo Bold",
                    foreground = colors[9],
                    padding = 2,
                    fontsize = 11
                ),
                widget.CurrentLayout(
                    foreground = colors[1],
                    padding = 5
                ),
                widget.TextBox(
                    text = '|',
                    font = "JetBrainsMono Nerd Font Propo Bold",
                    foreground = colors[9],
                    padding = 2,
                    fontsize = 11
                ),
                widget.WindowName(
                    foreground = colors[6],
                    padding = 8,
                    max_chars = 40
                ),
                widget.GenPollText(
                    update_interval = 300,
                    func = lambda: subprocess.check_output("printf $(uname -r)", shell=True, text=True),
                    foreground = colors[3],
                    padding = 8, 
                    fmt = '{}',
                ),
                sep,
                widget.CPU(
                    foreground = colors[4],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
                    format="CPU: {load_percent}%",
                ),
                sep,
                widget.Memory(
                    foreground = colors[8],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e btop')},
                    format = 'Mem: {MemUsed:.0f}{mm}',
                ),
                sep,
                widget.DF(
                    update_interval = 60,
                    foreground = colors[5],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-disk')},
                    partition = '/',
                    format = '{uf}{m} free',
                    fmt = 'Disk: {}',
                    visible_on_warn = False,
                ),
                sep,
                widget.Battery(
                    foreground=colors[6],           # pick a palette slot you like
                    padding=8,
                    update_interval=5,
                    format='{percent:2.0%} {char} {hour:d}:{min:02d}',  # e.g. "73% ⚡ 1:45"
                    fmt='Bat: {}',
                    charge_char='',               # shown while charging
                    discharge_char='',            # Nerd icon; use '-' if you prefer plain ascii
                    full_char='✔',                 # when at/near 100%
                    unknown_char='?',
                    empty_char='!', 
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn(terminal + ' -e upower -i $(upower -e | grep BAT)'),
                    },
                ),
                sep,
                widget.Volume(
                    foreground = colors[7],
                    padding = 8, 
                    fmt = 'Vol: {}',
                ),
                sep,
                widget.Clock(
                    foreground = colors[8],
                    padding = 8, 
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-date')},
                    format = "%a, %b %d - %H:%M",
                ),
                widget.Systray(padding = 6),
                widget.Spacer(length = 8),
            ],
            margin=[0, 0, 0, 0], 
            size=30
        ),
    ),
]

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
