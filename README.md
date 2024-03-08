# My dotfiles

These are my systems main dotfiles.

# My dotfiles

This directory contains the dotfiles for my system

## Requirements

Ensure you have the following installed on your system

### Git

```
pacman -S git
```

### Stow

```
pacman -S stow
```

## Installation

First, check out the dotfiles repo in your $HOME directory using git

```
$ git clone git@github.com/ethycS0/dotfiles.git
$ cd dotfiles
```

then use GNU stow to create symlinks

```
$ stow .
```
Create and manage directories as saved on the system.

## Backup

Additional dotfiles can be backed up.
Use following command for not having to delete original files.

```
$ stow --adopt .
```
