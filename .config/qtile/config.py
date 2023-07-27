
# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

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
    Key([mod], "d", lazy.spawn(launcher),
        desc="Launch rofi launcher"),


    # Kill window ---------------
    Key([mod], "q", lazy.window.kill(),
        desc="Kill active window"),


    # Control qtile ---------------
    Key([mod, ctrl], "r",
        lazy.reload_config(),
        lazy.spawn(notify_cmd + ' "Configuration Reloaded!"'),
        desc="Reload the config"),

    Key([mod, ctrl], "s",
        lazy.restart(),
        lazy.spawn(notify_cmd + ' "Restarting Qtile..."'),
        desc="Restart qtile"),

    Key([mod, ctrl], "q",
        lazy.shutdown(),
        lazy.spawn(notify_cmd + ' "Exiting Qtile..."'),
        desc="Shutdown qtile"),


    # Terminal -------------
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"),

    Key([mod, "shift"], "Return", lazy.spawn(terminal + ' --float'),
        desc="Launch floating terminal"),

    Key([mod, alt], "Return", lazy.spawn(terminal + ' --full'),
        desc="Launch fullscreen terminal"),


    # Switch focus --------------------
    Key([mod], "Left", lazy.layout.left(),
        desc="Move focus to left"),

    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus to right"),

    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus dowm"),

    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up"),


    # Move windows -----------------------------------
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to left"),

    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to right"),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up"),


    # Toggle floating & fullscreen ----------------------
    Key([mod], "space", lazy.window.toggle_floating(),
        desc="Toggle floating"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),


    # Control volume ----------------------------
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volume + ' --up'),
        desc="Raise speaker volume"),

    Key([], "XF86AudioLowerVolume", lazy.spawn(volume + ' --down'),
        desc="Lower speaker volume"),

    Key([], "XF86AudioMute", lazy.spawn(volume + ' --toggle'),
        desc="Toggle audio mute"),


    # Screenshot
    Key([], "Print", lazy.spawn(screenshot + ' --full'),
        desc="Take full screenshot"),

    Key([mod], "Print", lazy.spawn(screenshot + ' --crop'),
        desc="Take screenshot of region"),



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
    ]),



]
