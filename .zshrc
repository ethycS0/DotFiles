export TERM=xterm-256color
export PATH=$HOME/bin:/usr/local/bin:$PATH
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="robbyrussell"
export LD_LIBRARY_PATH=/usr/local/cuda/lib64
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
export QT_QPA_PLATFORMTHEME="qt6ct"
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

# Aliases
alias assist="cd /home/arjun/git-repos/LibreChat/ && sudo docker compose up -d"
alias cform='touch .clang-format && echo "IndentWidth: 8" > .clang-format'
alias llvmform='~/.local/share/nvim/mason/bin/clang-format --style=llvm --dump-config > .clang-format && sed -i "/^IndentWidth:/d" .clang-format && awk "/^\\.{3}/ {print \"IndentWidth: 8\"} 1" .clang-format > .clang-format.tmp && mv .clang-format.tmp .clang-format && sed -i "/^ColumnLimit:/d" .clang-format && awk "/^\\.{3}/ {print \"ColumnLimit: 100\"} 1" .clang-format > .clang-format.tmp && mv .clang-format.tmp .clang-format'
alias vim="nvim"
alias vi="nvim"
alias lsp=" nvim ~/.config/nvim/lua/custom/configs/lspconfig.lua"
alias rc="nvim ~/.zshrc"
alias newmux='tmux new-window -n neovim nvim'
alias ffox="firefox 'file://$(pwd)'"
# Games
alias minecraft="__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia java -jar /home/arjun/Games/SKlauncher*"
alias nesdev="cd ~/Documents/Emulators/NES-Emulator && tmux"

# Embedded
alias ocd-c6="sudo /home/arjun/opt/STM32/com.st.stm32cube.ide.mcu.externaltools.openocd.linux64_2.3.200.202404091248/tools/bin/openocd -s /usr/share/openocd/scripts -f /usr/share/openocd/scripts/board/stm32c031c6.cfg "

# Maintainence
alias mirror-backup="sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak"
alias mirror-ayu="sudo reflector --latest 5 --country India --sort rate --save /etc/pacman.d/mirrorlist --protocol https --download-timeout 15"

# Fan control and Power Management
alias ft='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 1 >>  fan_boost_mode"; sudo sh -c "echo 1 >> throttle_thermal_policy"; source ~/.zshrc; cd ~;'
alias fp='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 0 >>  fan_boost_mode"; sudo sh -c "echo 0 >> throttle_thermal_policy"; source ~/.zshrc; cd ~;'
alias fs='cd /sys/devices/platform/asus-nb-wmi; sudo sh -c "echo 2 >>  fan_boost_mode"; sudo sh -c "echo 2 >> throttle_thermal_policy"; source ~/.zshrc; cd ~;'
alias fan-ayu="cat /sys/devices/platform/asus-nb-wmi/fan_boost_mode"
alias batteryInf="cat /sys/class/power_supply/BAT0/capacity"

# Virtualization
alias win="sh /home/arjun/VM-scripts//winvm.sh"

# Peripherals
alias red="redshift -l 18.51957:73.85535 &"
alias bri="ddcutil setvcp 10"
alias mouse-reset="xinput --set-prop 12 'libinput Accel Profile Enabled' 0, 1"

# Networking
alias mon-mode="sudo airmon-ng check kil && sudo airmon-ng start wlo1"
alias norm-mode="sudo airmon-ng stop wlo1mon && sudo systemctl start NetworkManager"

# GDB and gcc
alias peda_gdb='rm ~/.gdbinit && echo "source ~/peda/peda.py" >> ~/.gdbinit'
alias gef_gdb='bash -c "$(wget https://gef.blah.cat/sh -O -)"'
alias cross-gcc="$HOME/opt/cross/bin/i686-elf-gcc"
alias cross-as="$HOME/opt/cross/bin/i686-elf-as"
alias cross-ld="$HOME/opt/cross/bin/i686-elf-ld"
