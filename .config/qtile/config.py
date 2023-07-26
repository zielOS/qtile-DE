
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
term = "qterm" 
launcher = "qmenu"
browser = "brave"
gui_file_manager = "dolphin"
gui_editor = "emacsclient -c -a emacs"
tui_editor = "alacritty -e lvim"
tui_file_manager = "alacritty -e ranger"

keys = [
    # Launcher ------------
    Key([mod], "d", lazy.spawn(launcher),
        desc="Launch rofi launcher"),


    # Control qtile ----------
    Key([mod, ctrl], "r", lazy.reload_config(),
        desc="Reload the config"),

    Key([mod, ctrl], "s", lazy.restart(),
        desc="Restart qtile"),

    Key([mod, ctrl], "q", lazy.shutdown(),
        desc="Shutdown qtile"),


    # Terminal -------------
    Key([mod], "Return", lazy.spawn(term),
        desc="Launch terminal"),

    Key([mod, "shift"], "Return", lazy.spawn(term + ' --float'),
        desc="Launch floating terminal"),

    Key([mod, alt], "Return", lazy.spawn(term + ' --full'),
        desc="Launch fullscreen terminal"),


    # Switch focus between windows
    Key([mod], "Left", lazy.layout.left(),
        desc="Move focus to left"),

    Key([mod], "Right", lazy.layout.right(),
        desc="Move focus to right"),

    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus dowm"),

    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to left"),

    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to right"),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up"),


    # Toggle floating & fullscreen
    Key([mod], "space", lazy.window.toggle_floating(),
        desc="Toggle floating"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),


    # Gui apps ----------
    KeyChord([mod], "g", [
        Key(
            [], "b",
            lazy.spawn(browser),
            desc="Launch web browser"
            ),
        Key(
            [], "f",
            lazy.spawn(gui_file_manager),
            desc="Launch file-manager"
            ),
        Key(
            [], "e",
            lazy.spawn(gui_editor),
            desc="Launch emacs"
            ),
    ]),

    # Tui apps ----------------------
    KeyChord([mod], "t", [
        Key(
            [], "l",
            lazy.spawn(tui_editor),
            desc="Launch lvim"
            ),
        Key(
            [], "r",
            lazy.spawn(tui_file_manager),
            ),
    ]),

    Key(


    
        ),



]
