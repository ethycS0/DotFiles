#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Maintainence
alias mirror-backup="sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak"
alias mirror-ayu="sudo reflector --latest 5 --country India --sort rate --save /etc/pacman.d/mirrorlist --protocol https --download-timeout 15"


# Wifi
alias wifi-ethycS="nmcli device wifi connect ethycS password wRongPassword:3"

# Fan control and Power Management
alias fan-turbo='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 1 >>  fan_boost_mode"; sudo sh -c "echo 1 >> throttle_thermal_policy"; source ~/.bashrc; cd ~;'
alias fan-performance='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 0 >>  fan_boost_mode"; sudo sh -c "echo 0 >> throttle_thermal_policy"; source ~/.bashrc; cd ~;'
alias fan-silent='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 2 >>  fan_boost_mode"; sudo sh -c "echo 2 >> throttle_thermal_policy"; source ~/.bashrc; cd ~;'
alias fan-ayu="cat /sys/devices/platform/asus-nb-wmi/fan_boost_mode"

# Virtualization
alias win="sh /home/arjun/winvm.sh"

# Peripherals
alias bri="ddcutil setvcp 10"
alias mouse-reset="xinput --set-prop 16 'libinput Accel Profile Enabled' 0, 1"

# Networking
alias mon-mode="sudo airmon-ng check kil && sudo airmon-ng start wlo1"
alias norm-mode="sudo airmon-ng stop wlo1mon && sudo systemctl start NetworkManager"
