## CloseFolder Sublime Text plugin

[![Package Control](https://img.shields.io/packagecontrol/dt/CloseFolder.svg)](https://packagecontrol.io/packages/CloseFolder)
[![GitHub tag](https://img.shields.io/github/tag/aviaryan/CloseFolder.svg)](https://github.com/aviaryan/CloseFolder/releases)

A simple Sublime Text plugin to close all open files of current directory or all open files inside some directory. Supports Sublime Text 2 and 3.


### Motivation

1. When doing web development project, the tab count easily shoots up to 30+ in no time. By this time, figuring each tab starts becoming difficult as only few characters of the filename can be seen. With this I can quickly close an *old* folder (which I may not need now) and generate some room.
2. I keep all my college semester lab work in a single project. Whenever I need to make some room, I close a past 'lab' folder.
3. When I take part in a coding contest/marathon, I create a folder for it and then keep all related files in there. By the end of the contest, I easily have 10+ tabs opened for it. This plugin helps me remove them all at once.


### Installing

Search for `CloseFolder` and install it via [Package Control](https://packagecontrol.io).

OR

[Download this repo](https://github.com/aviaryan/CloseFolder/archive/master.zip), extract it and then place *CloseFolder* folder in Packages directory of ST.


### Using

There are 2 commands in this plugin.

1. `close_folder` - Closes all files which are in the same directory (& below) as the file opened in the active tab. This can be activated by following ways.

	1. Right click in the *Sublime Text editing area* and select 'Close Folder' option.
	2. Open Command Palette (Ctrl-Shift-P) and run `CloseFolder: Close all files in this folder recursively`.

2. `close_folder_dirs `- Closes all files which are inside the selected directory, recursively. This can be activated from the **sidebar** by right clicking on the folder and selecting 'Close Folder' option.


### Screenshots

| ![screen shot 2017-01-12 at 5 56 46 pm](https://cloud.githubusercontent.com/assets/4047597/21889999/9fce05d4-d8f1-11e6-94d1-76c0c05dc5e0.png) | ![screen shot 2017-01-12 at 6 02 22 pm](https://cloud.githubusercontent.com/assets/4047597/21890001/a0ab27f2-d8f1-11e6-9941-b12e6d90f9c1.png) |
|----|----|
| ![stcp](https://cloud.githubusercontent.com/assets/4047597/23291911/b3a75b6c-fa81-11e6-9257-409f00d0aeae.png) | ![potato](https://cloud.githubusercontent.com/assets/4047597/23291941/e9c05776-fa81-11e6-886c-c2da6d44e4d1.jpg) |
