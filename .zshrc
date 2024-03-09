export PATH=$HOME/bin:/usr/local/bin:$PATH
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"

# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"
# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"
zstyle ':omz:update' mode auto  # just remind me to update when it's time
zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"
# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"
# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"
# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

plugins=(
  git 
  zsh-syntax-highlighting
  tmux
)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"
#
TERM=xterm-256color
#
# Aliases

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
