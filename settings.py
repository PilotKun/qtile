import os

mod = "mod4"
terminal = "alacritty"
USER_HOME = os.path.expanduser("~")
volume_step = 5
brightness_step = 5

commands = dict(
    terminal="alacritty",
    nvim="nvim",
    kill_window="xkill",
    toggle_mute_mic="amixer set Capture toggle",
    rofi="rofi -show drun",
    brave="brave",
    flameshot="flameshot gui",
    poweroff="poweroff",
    reboot="reboot",
    raise_volume=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/audio.sh raise {volume_step}",
    lower_volume=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/audio.sh lower {volume_step}",
    switch_audio_sink=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/audio.sh switch_sink",
    toggle_mute=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/audio.sh mute",
    brightness_up=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/brightness.sh raise {brightness_step}",
    brightness_down=f"sh {USER_HOME}/nixos-dots/config/qtile/scripts/brightness.sh lower {brightness_step}",
)
