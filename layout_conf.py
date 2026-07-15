from libqtile.config import Match
from libqtile import layout
from settings import layout_default

###########
# LAYOUTS #
##########

layout_theme = {
    "border_width" : 2,
    "margin" : 5,
    "border_focus" : colors[6],
    "border_normal" : colors[0],
}

layouts = [
    layout.Columns(**layout_default),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Floating window config (different from the layout)
floating_layout = layout.Floating(
    **layout_default.extend(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(wm_class="flameshot"),  # Flameshot upload window
            Match(wm_class="pavucontrol"),  # Pulse Audio Volume Control
            Match(wm_class="helvum"),  # Volume control GUI for Pipewire
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ],
    ),
)
