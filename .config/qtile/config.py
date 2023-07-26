
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
terminal = "qterm" 
launcher = "qmenu"
browser = "brave"
gui_file_manager = "dolphin"
gui_editor = "emacsclient -c -a emacs"
tui_editor = "alacritty -e lvim"
tui_file_manager = "alacritty -e ranger"

keys = [
    # Launcher ------------
    Key(
        [mod], "d",
        lazy.spawn(launcher),
        desc="Launch rofi launcher"
        ),

    # Terminal -------------
    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn(terminal + ' --float'),
        desc="Launch floating terminal"
        ),
    Key(
        [mod, alt], "Return",
        lazy.spawn(terminal + ' --full'),
        desc="Launch fullscreen terminal"
        ),


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


	# Function keys : Volume --
    Key(
		[], "XF86AudioRaiseVolume", 
		lazy.spawn(volume + ' --inc'),
		desc="Raise speaker volume"	
	),
    Key(
		[], "XF86AudioLowerVolume", 
		lazy.spawn(volume + ' --dec'),
		desc="Lower speaker volume"	
	),
    Key(
		[], "XF86AudioMute", 
		lazy.spawn(volume + ' --toggle'),
		desc="Toggle mute"	
	),
    Key(
		[], "XF86AudioMicMute", 
		lazy.spawn(volume + ' --toggle-mic'),
		desc="Toggle mute for mic"
	),
]
