from libqtile import layout
from libqtile.config import Match
from .theme import colors


layouts = [
    layout.Columns(
        border_width=1,
        border_focus=colors['focus'][0],
        margin=4,
    ),
    layout.MonadTall(
        border_width=1,
        border_focus=colors['focus'][0],
        margin=4,
    ),
    # layout.Max(),
    # layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)
