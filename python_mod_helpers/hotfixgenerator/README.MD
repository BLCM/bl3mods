# DESCRIPTION

This application is a WIP tool for modders to help streamline the process of finding information and creating. bl3hotfix mods

# NOTE

I am a college student, so I will not be able to work on this all the time, but I will when I have free time.
This will be a massive passion project for me, so there will be many errors and bugs in my program.
Feedback and tips for how to improve this program are appreciated. I will get to them as soon as I can.
If you are curious about something or have a question about something, the best way to contact me is via my email, which you can find in my profile, or send me a message on Discord.

# GETTING STARTED

Currently, I do not have a .exe that runs everything and everything is magically ready.
Unfortunately, you will need to do some extra work before you can get started.
To get started, you will want the following:

1. My `py_check.bat` will attempt to get python and install it for you, but if you already have python or you want to install it manually, go to the next step
2. Python installed: https://www.python.org/downloads/
   1. Once you have it installed, double-click on the file called `py_libs.py`
      1. If this does not work on your machine,
   2. This runs a script that installs all the needed Python Libraries.
      1. This may take a minute as I also slight modify one of the installed libaries to make this program work.
3. A program that runs Python IDE's': https://realpython.com/python-ides-code-editors-guide/
4. A file editor (EX: Notepad++). The basic Notepad will work, but is harder to use.

My recommendation is VScode.

1. Download: https://code.visualstudio.com/download
2. Also get this this extention for  VSCode: https://marketplace.visualstudio.com/items?itemName=ms-python.python
3. It acts like a Python IDE and can very easily edit code at the same time.

## Caveats

Even after doing the above, running the program will still not work, and here is why.

Variables in bl3data.py: variable `data_dir`, `ueserialize_path` and function `_connect_db`. This is because I can not include them as they are external products and can not included them, but I will describe how to get them and use them

## Instructions

Steps to fully utilize the program.
Instructions are based in Windows, so Linux and Mac users commands will be slightly different
**NOTE:** You will need to be able to open bl3data.py to edit variables.

1. `data_dir`: **Note:** You will need a copy of BL3. Duh

   1. Follow instructions at: https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data
      1. These instructions are extremly useful, and do a better job of explaining than me.
   2. Once you have extracted all the data, place the `extracted_new` folder inside the hotfixgenerator folder, the program will do the rest
   3. If you are unable to follow these steps, go to this link and download the seralized files
      1. These may not be the most up to date version of the game when you get them, so just be aware.
      2. **NOTE**: this will be a large download: https://www.nexusmods.com/borderlands3/mods/247
2. `ueserialize_path`

   1. Go and download this .exe from this link: https://github.com/apocalyptech/JohnWickParse/releases/download/v19/john-wick-parse.exe
   2. Once you have done that, grab the .exe and move it inside the hotfixgenerator folder.
3. `_connect_db`

   1. Go to think link and download this file: https://apocalyptech.com/games/bl3-refs/bl3refs.sqlite3.zip
   2. Extract the file and put the bl3refs.sqlite3 file inside the hotfixgenerator.
4. If something went wrong or you want to change the file locations, go to this file location:

   1. `C:\Users\<Name>\AppData\Local\bl3data\bl3data\bl3data.ini` (`<Name>` will be different depending on your computer)
   2. Open the file and manually change the paths to the correct path. The basic Notepad should work fine

# CREDITS

I did not create all of these files, most of the hard work was already done.
List of resources that have helped me:

- apocalyptech: Researcher and provided many of the resources I have used.
  - GitHub: https://github.com/apocalyptech
  - Specific repository I pulled from: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
  - SQL File and Object Reference: https://apocalyptech.com/games/bl3-refs/
- BL3 Redux Team: They inspired me to try and make this because I saw all the changes they did and what you can do with this game.
  - Link to the hotfix: https://github.com/BLCM/bl3mods/tree/master/EpicNNG
