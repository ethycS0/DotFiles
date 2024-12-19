
# Peripherals
xinput --set-prop "$(xinput list | grep 'Razer Razer DeathAdder Essential' | grep -m1 -o 'id=[0-9]\+' | cut -d= -f2)" 'libinput Accel Profile Enabled' 0, 1
# Display
xrandr --output HDMI-1-0 --mode 1920x1080 --rate 165 --primary
xrandr --output eDP-1 --mode 1920x1080 --rate 144 --left-of HDMI-1-0
redshift -l 18.51957:73.85535 &

# Startup
/usr/bin/dunst &
nitrogen --restore &
asusctl profile -P quiet &
caps2esc -m 2 &
otd-daemon &
flameshot &
qtile start
