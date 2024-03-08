from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.base import base, powerline, rectangle, symbol
from extras import Clock, GroupBox, TextBox, modify, widget
from utils.config import cfg
from utils.palette import palette

bar = {
    "background": palette.base,
    "border_color": palette.base,
    "border_width": 4,
    "margin": [0, 0, 0, 0],
    "opacity": 1,
    "size": 24,
}


def sep(fg, offset=0, padding=10):
    return TextBox(
        **base(None, fg),
        **symbol(11),
        offset=offset,
        padding=padding,
        text="󰇙",
    )


logo = lambda bg, fg: TextBox(
    **base(bg, fg),
    **symbol(),
    **rectangle(),
    mouse_callbacks={"Button1": lazy.restart()},
    padding=15,
    offset=-4,
    text=" ",
)

groups = lambda bg: GroupBox(
    **symbol(),
    background=bg,
    borderwidth=1,
    colors=[
        palette.teal,
        palette.pink,
        palette.yellow,
        palette.red,
        palette.blue,
        palette.green,
    ],
    highlight_color=palette.base,
    highlight_method="line",
    inactive=palette.surface2,
    invert=True,
    padding=6,
    rainbow=True,
)

volume = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(),
        **rectangle("left"),
        offset=-17,
        padding=15,
        text="",
        x=-2,
    ),
    widget.Volume(
        **base(bg, fg),
        **powerline("arrow_right"),
        check_mute_command="pamixer --get-mute",
        check_mute_string="true",
        get_volume_command="pamixer --get-volume-human",
        mute_command="pamixer --toggle-mute",
        update_interval=0.1,
        volume_down_command="pamixer --decrease 5",
        volume_up_command="pamixer --increase 5",
        font="JetBrainsMono Nerd Font",
        fontsize=10,
    ),
]

window_name = lambda fg: widget.WindowName(
    **base(None, fg),
    format="{name}",
    max_chars=60,
    width=CALCULATED,
    font="JetBrainsMono Nerd Font",
    fontsize="10",
)

cpu = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-13,
        padding=15,
        text="󰍛",
    ),
    widget.CPU(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{load_percent:.0f}%",
        font="JetBrainsMono Nerd Font",
        fontsize="10",
    ),
]

ram = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        padding=5,
        text="󰘚",
    ),
    widget.Memory(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{MemUsed: .0f}{mm} ",
        padding=-3,
        font="JetBrainsMono Nerd Font",
        fontsize="10",
    ),
]

backlight = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=3,
        padding=2,
        text="󰃠",
    ),
    widget.Backlight(
        **base(bg, fg),
        **rectangle("right"),
        backlight_name="intel_backlight",
        brightness_file="/sys/class/backlight/intel_backlight/brightness",
        max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
        change_command="light -S {0:.0f}",
        scroll=True,
        padding=None,
        font="JetBrainsMono Nerd Font",
        fontsize=10,
    ),
]



disk = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=2,
        text="",
        x=-2,
    ),
    widget.DF(
        **base(bg, fg),
        **rectangle("right"),
        format="{f} GB  ",
        padding=0,
        partition="/",
        visible_on_warn=False,
        warn_color=fg,
        font="JetBrainsMono Nerd Font",
        fontsize="10",
    ),
]

clock = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-10,
        padding=15,
        text="",
    ),
    modify(
        Clock,
        **base(bg, fg),
        **rectangle("right"),
        format="%A - %I:%M %p ",
        long_format="%B %-d, %Y ",
        padding=7,
        font="JetBrainsMono Nerd Font",
        fontsize="10",
    ),
]


widgets = lambda: [
    widget.Spacer(length=1),
    logo(palette.blue, palette.base),
    sep(palette.surface2, offset=-14),
    groups(None),
    sep(palette.surface2, offset=8, padding=2),
    *volume(palette.pink, palette.base),
    *backlight(palette.blue, palette.base),
    widget.Spacer(),
    window_name(palette.text),
    widget.Spacer(),
    *cpu(palette.green, palette.base),
    *ram(palette.yellow, palette.base),
    *disk(palette.teal, palette.base),
    sep(palette.surface2),
    *clock(palette.pink, palette.base),
    widget.Spacer(length=1),
]
