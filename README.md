# Install Window Manager on Qtile
 
## 1. Install Qtile
 
How to install Qtile Step by Step between Ubuntu/Debian and Arch Linux
 
### Install Qtile on Ubuntu/Debain
 
Install the packages with Python-pip:
```
sudo apt install python3-pip
pip install xcffib
pip install qtile
```

Edit to create file on XSession and where the router of root:
```
cd /usr/share/xsessions/
sudo touch qtile.desktop
sudo nvim qtile.desktop
```

And the texts copy and paste on XSession and then save to file.
```
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wm;tiling
```

### Install Qtile on Arch/Manjaro

Installed is very easy  a line of commands on terminal:
```
sudo pacman -S qtile
```
