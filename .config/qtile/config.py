
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

# Mouse
from libqtile.config import Click, Drag

# Groups
from libqtile.config import Group, Match

# Layouts
from libqtile import layout

# Screens
from libqtile.config import Screen
from libqtile import bar, widget

# ScratchPad and DropDown
from libqtile.config import ScratchPad, DropDown

# Startup
import os
import subprocess
from libqtile import hook


## Startup ------------------------------
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.local/bin/qstart'])





NUM_SCREENS = 3
NUM_GROUPS = 8
GROUP_MAP = {}
GROUP_LIST = []

# Here we create two objects:
# 1) A dict, "GROUP_MAP", which has a key relating to the screen index. The value is another dict
#    where groups are numbered from 1 to NUM_GROUPS. The value is a unique group name.
# 2) A list of all groups. Each group has a unique name but the label is between 1 and NUM_GROUPS
for screen in range(NUM_SCREENS):
    screen_dict = {}
    for group in range(NUM_GROUPS):
        name = f"{screen * NUM_GROUPS + group}"
        group_num = group + 1
        screen_dict[group_num] = name
        GROUP_LIST.append(Group(name, label=str(group_num)))
    GROUP_MAP[screen] = screen_dict

@lazy.function
def switch_group(qtile, group_num):
    """
    This function looks up the unique group name for group number on the current screen
    and then displays that group.
    """
    group_name = GROUP_MAP[qtile.current_screen.index + 1][group_num]
    qtile.groups_map[group_name].toscreen()


@lazy.window.function
def move_window_to_group(window, group_num, switch_group=False, toggle=False):
    """
    This function looks up the unique group name for group number on the current screen
    and then moves the window to that group.
    """   
    group_name = GROUP_MAP[window.qtile.current_screen.index + 1][group_num]
    window.togroup(group_name, switch_group, toggle)

# Groups should be set to our group list
groups = GROUP_LIST

# We bind keys mod + 1-8 to call our function to display a group depending on the focused screen
# mod + shift + 1-8 moves window to that group on the active screen
for i in range(NUM_GROUPS):
    keys.append(Key([mod], str(i + 1), switch_group(i + 1)))
    keys.append(Key([mod, "shift"], str(i + 1), move_window_to_group(i + 1, switch_group=True)))

# mod + control + 1-3 moves window to current group on that screen
for i in range(NUM_SCREENS):
    keys.append(Key([mod, "control"], str(i + 1), lazy.window.toscreen(i)))

    # def init_keys_groups(self, group_names):
    # """
    # Create bindings to move between groups
    # """
    # @lazy.function
    # def switch_groups(qtile, group_name):
    #     current_screen_index = qtile.screens.index(qtile.current_screen)
    #     layout_index = "monadtall"
    #     if current_screen_index == 0:
    #         layout_index = "monadtall"
    #     elif current_screen_index > 0:
    #         layout_index = "monadwide"
    #     for g in qtile.groups:
    #         if g.name == group_name:
    #             # change to g.tooscreen() when it's released from git
    #             g.cmd_toscreen()
    #             # change to qtile.cmd_to_layout_index when it's released from git
    #             g.cmd_setlayout(layout_index)
    #             return

    # group_keys = []
    # for group_name in group_names:
    #     index = (group_name[0]).lower()
    #     group_keys += [Key([MOD], index, switch_groups(group_name)), Key(
    #         [MOD, SHIFT], index, lazy.window.togroup(group_name, switch_group=False))]

    # return group_keys
