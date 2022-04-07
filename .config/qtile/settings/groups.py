from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys


 # 2: Group("  ", matches=[Match(wm_class=["firefox"])]),

groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ",  "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

