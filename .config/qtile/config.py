# https://docs.qtile.org/en/latest/_modules/libqtile/config.html
# https://docs.qtile.org/en/latest/manual/config/index.html
# https://docs.qtile.org/en/stable/manual/ref/widgets.html
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import psutil
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
from core.bar import Bar
from utils.config import cfg
from utils.palette import palette
from utils.match import title, wm_class


mod = "mod4"
terminal = "alacritty"

def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help

keys = [

    Key([mod], "Return", lazy.spawn(terminal), desc="Launches My Terminal"),
    Key(
        [mod],
        "d",
        lazy.spawn("sh /home/arjun/.config/rofi/launchers/type-1/launcher.sh"),
        desc="Rofi app launcher",
    ),
    Key([mod], "w", lazy.window.kill(), desc="Kill active window"),
    Key(
        [mod, "shift"],
        "r",
        lazy.restart(),
        # lazy.spawn("reopen_eww.sh"),
        desc="Restart Qtile",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(" sh /home/arjun/.config/rofi/applets/bin/powermenu.sh"),
        desc="Power Menu",
    ),
    Key(
        [mod, "shift"],
        "a",
        lazy.spawn("flameshot gui"),
        desc="Screenshot",),

    Key(
        [mod], "j", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod],
        "h",
        lazy.layout.left(),
        # lazy.layout.next(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.right(),
        # lazy.layout.previous(),
        desc="Move focus right in current stack pane",
    ),
    # Move windows within group
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        # lazy.layout.swap_left(),
        # lazy.layout.client_to_previous(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        # lazy.layout.swap_right(),
        # lazy.layout.client_to_next(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    # Flip layouts for bsp
    Key(
        [mod, "control"],
        "j",
        lazy.layout.flip_down(),
        # lazy.layout.section_down(),
        # lazy.layout.integrate_down(),
        desc="Flip layout down",
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.flip_up(),
        # lazy.layout.section_up(),
        # lazy.layout.integrate_up(),
        desc="Flip layout up",
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left(),
        # lazy.layout.integrate_left(),
        desc="Flip layout left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.flip_right(),
        lazy.layout.swap_column_left(),
        # lazy.layout.integrate_right(),
        desc="Flip layout right",
    ),
    # Resize windows
    Key(
        [mod, "mod1"],
        "h",
        resize_left,
        # lazy.layout.grow_width(-30),
        desc="Resize window left",
    ),
    Key(
        [mod, "mod1"],
        "l",
        resize_right,
        # lazy.layout.grow_width(30),
        desc="Resize window Right",
    ),
    Key(
        [mod, "mod1"],
        "k",
        resize_up,
        # lazy.layout.grow_height(30),
        desc="Resize windows upward",
    ),
    Key(
        [mod, "mod1"],
        "j",
        resize_down,
        # lazy.layout.grow_height(-30),
        desc="Resize windows downward",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.normalize(),
        # lazy.layout.reset_size(),
        desc="Normalize window size ratios",
    ),
    # Window States
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on focused window",
    ),
    Key(
        [mod],
        "Up",
        lazy.window.toggle_minimize(),
        desc="Toggle minimization on focused window",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.group.unminimize_all(),
        desc="Unminimize all windows on current group",
    ),
    Key([mod], "a",lazy.spawn("firefox"),
        desc="Launch Firefox"),

Key(
        [mod],
        "backslash",
        lazy.spawn("dolphin"),
        desc="Launch files",
    ),
]

groups = [Group(i) for i in "12345"]

colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 2,
    "border_focus": "002FFF",
    "border_normal": "01060E",
    "font": "JetBrainsMono Nerd Font",
    "grow_amount": 2,
}

layouts = [
      layout.Bsp(**layout_theme, fair=False, border_on_single=True),
      layout.Floating(**layout_theme),
]

screens = [
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
        top=Bar(cfg.bar).create(),
    ),
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
        top=Bar(cfg.bar).create(),
    ),
    
]


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False 
bring_front_click = "floating_only"
floats_kept_above = True
cursor_warp = False


floating_layout = layout.Floating(
    border_focus=palette.subtext1,
    border_normal=palette.base,
    border_width=3,
    fullscreen_border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        *wm_class(
            "confirmreset",
            "Display",
            "floating",
            "gnome-screenshot",
            "gpicview",
            "kvantummanager",
            "lxappearance",
            "makebranch",
            "maketag",
            "pavucontrol",
            "pinentry-gtk-2",
            "psterm",
            "qt5ct",
            "ssh-askpass",
            "steam",
            "thunar",
            "Thunar",
            "Xephyr",
            "xfce4-about",
        ),
        *title(
            "branchdialog",
            "minecraft-launcher",
            "pinentry",
        ),
    ],
)
x11_drag_polling_rate = 165
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None


wmname = "LG3D"
