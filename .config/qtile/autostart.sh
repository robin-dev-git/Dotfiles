#!/bin/sh
##xrandr --output HDMI-1 --primary 1920x1080 --pos 0x0 &
#xrandr --output eDP-1 --primary --mode 1280x800 --pos 0x0 &
setxkbmap latam &
#feh --bg-fill ~/.config/qtile/wallpaper.jpg
#picom --no-vsync &
nitrogen --restore &
picom -f &
#udiskie -t &
nm-applet &
#volumeicon &
cbatticon &
