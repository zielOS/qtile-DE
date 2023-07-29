from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
import os

# Variables:
mod = "mod4"
alt = "mod1"
ctrl = "control"


# Scripts
home = os.path.expanduser('~')
terminal = home + '/.local/bin/qterm'
volume = home + '/.local/bin/qvolume'
launcher = home + '/.local/bin/qmenu'
screenshot = home + '/.local/bin/qscreenshot'
browser = 'brave'
gui_file_manager = 'thunar'
gui_editor = 'emacsclient -c -a emacs'
tui_editor = 'alacritty -e lvim'
tui_file_manager = 'alacritty -e ranger'
notify_cmd = 'dunstify -u low -h string:x-dunst-stack-tag:qtileconfig'

keys = [
    # Launcher ---------------------
    Key([mod], "d", lazy.spawn(launcher)),

    # Control qtile ---------------
    Key([mod, ctrl], "r",
        lazy.reload_config(),
        lazy.spawn(notify_cmd + ' "Configuration Reloaded!"')),

    Key([mod, ctrl], "s",
        lazy.restart(),
        lazy.spawn(notify_cmd + ' "Restarting Qtile..."')),

    Key([mod, ctrl], "q",
        lazy.shutdown(),
        lazy.spawn(notify_cmd + ' "Exiting Qtile..."')),


    # Terminal -------------
    Key([mod], "Return", lazy.spawn(terminal)),

    Key([mod, "shift"], "Return", lazy.spawn(terminal + ' --float')),

    Key([mod, alt], "Return", lazy.spawn(terminal + ' --full')),

    # Kill window ---------------
    Key([mod], "q", lazy.window.kill()),

    # Switch focus --------------------
    Key([mod], "Left", lazy.layout.left()),

    Key([mod], "Right", lazy.layout.right()),

    Key([mod], "Down", lazy.layout.down()),

    Key([mod], "Up", lazy.layout.up()),


    # Move windows -----------------------------------
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),

    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),


    # Resize windows
    Key([mod, ctrl], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete()),

    Key([mod, ctrl], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add()),

    Key([mod, ctrl], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster()),

    Key([mod, ctrl], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster()),


    # Toggle floating & fullscreen ----------------------
    Key([mod], "space", lazy.window.toggle_floating()),

    Key([mod], "f", lazy.window.toggle_fullscreen()),


    # Control volume ----------------------------
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volume + ' --up')),

    Key([], "XF86AudioLowerVolume", lazy.spawn(volume + ' --down')),

    Key([], "XF86AudioMute", lazy.spawn(volume + ' --toggle')),


    # Screenshot
    Key([], "Print", lazy.spawn(screenshot + ' --full')),

    Key([mod], "Print", lazy.spawn(screenshot + ' --crop')),


    # Gui apps ----------
    KeyChord([mod], "g", [
        Key([], "b", lazy.spawn(browser),
            desc="Launch web browser"),

        Key([], "f", lazy.spawn(gui_file_manager),
            desc="Launch file-manager"),

        Key([], "e", lazy.spawn(gui_editor),
            desc="Launch emacs"),
    ]),


    # Tui apps ----------------------
    KeyChord([mod], "t", [
        Key([], "l", lazy.spawn(tui_editor),
            desc="Launch lvim"),

        Key([], "r", lazy.spawn(tui_file_manager),
            desc="Launch ranger"),
    ])
]
