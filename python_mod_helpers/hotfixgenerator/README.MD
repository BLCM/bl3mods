# DESCRIPTION

This application is a WIP tool for modders to help streamline the process of finding information and creating .bl3hotfix mods

# NOTE

I am a college student, so I will not be able to work on this all the time, but I will when I have free time.
This will me a massive passion project for me, so there will be many errors and bugs in my program.

Feedback and tips for how to improve this program are appreciated. I will get to them as soon as I can.

If you are curious about something or have a question about something, best way to contact me is via my email, which you can find in my profile, or send me a message on Discord

# USEAGE

Currently I do not have a .exe that magically runs everything you need and makes it work perfectly.

In order to get this tool working, you will need a program that runs Python programs.

My personal recomendation is VScode, and install the Python extention. However any program that runs Python scrips should work fine.

You will need to install Python on your computer. Link: https://www.python.org/downloads/

I have created a .bat file that you can run to install all the needed python libaries.

## Tool Caveats

The program will not work proporly even if you have Python and ran the .bat file, but they are important steps.

This is because variables in bl3data.py, `'data_dir'`, `'ueserialize_path'`, and the database functions will be unique for each person.

In the future I wish to solve the database issue by making a public one, but for the other variables you will have to do that on your own.

## Instructions

Instructions to fully utilize the program. **NOTE:**  You will have to go into the bl3data.py file and instert the needed information.

1. 'data_dir': **Note:** You will need a copy of BL3. Duh
   1. Follow instructions at: https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data
   2. Once you have extracted all the data, set 'data_dir' as the extracted_new file path.
      1. EX: ''F:/Users/Name/Desktop/extracted_new''
   3. If you do not own the game but still want to use this program(?), there is an alternative way to get the seralized files but I do not feel comfortable putting in the link in, as I do not know if it is ok to get the seralized game files without actually owning. If it turns out it is ok, I will put in the link, otherwise I will remove this section talking about it
      1. **NO I AM NOT TALKING ABOUT PIRATING, DO NOT PIRATE THE GAME PLEASE**
      2. The only hint I will give is to look into the BL3 nexus page.
      3. If you find what I am referencing, be aware that even if you have thoses files, I am not fully sure that the program will work.
         1. I have not tested because I already bought the games and extrated the data, and I do not want to test it out because thats a lot of work and I just don't want to really
2. 'ueserialize_path': This can be confusing, so here are the steps i took to make it work.
   1. Download the file from here: https://github.com/apocalyptech/JohnWickParse
   2. Extract the file into a good location.
   3. Open up command line and type cd <Location/Of/Extracted/JohnWickParse>, then hit enter.
   4. Click this link and run the .exe file: https://win.rustup.rs/
   5. Once you have run that, go back you your command line and type cargo build.
      1. This may take a minute, so be patient with it.
   6. One it is done building, get the file location where the debug file is.
   7. Get that file path and set 'ueserialize_path' equal to that.
      1. EX: ''F:/Users/Name/Desktop/extracted_new/JohnWickParse-indexed_arrays/target/debug''
   8. If something went wrong or you want to change where they are located, go to this file location:
      1. C:\Users\Name\AppData\Local\bl3data\bl3data\bl3data.ini (Example)
      2. Open it and manually change the paths to the correct path.

This is a "Optional" step, as you do not technically need a database to make the program, however you will be missing out on some features that this tool has.

1. Data Base connections.
   1. In bl3data.py, I have modified the '`_connect_db`' function to use `pyodbc` connections.
   2. If you have a SQL server (SQLEXPRESS for example) and know how to insert information, then you would be able to use your own tables and database to pull information from.
      1. This is what I have done, as I already had Database up, so I just inserted the information.
      2. You may change the _connect_db section to whatever python DB connector you want, but this is what I have personally done.
   3. You will need apocalyptech MariaDB datadump, Link to this in the Credits.
      1. I have left my formatting files in 'Extra_Files' folder.
      2. **NOTE**: I did not comment my formatter files well. Reason being that it was a mach program I made to ease my pain. You will more than likely encounter erros, but I beleive in you.
   4. You will also want a SQL formatter. Link also in the Credits.

# CREDITS

I did not create all of these files, most of the hard work was already done.
What I am doing is makeing a program stream lines the process of making BL3 mods

List of resources that have helped me:

- apocalyptech: This program is heavly based on the research and projects
  - Github: https://github.com/apocalyptech
  - Specific reposatory I pulled from: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
  - SQL File and Object Reference: https://apocalyptech.com/games/bl3-refs/
- Site that help format the SQL file: https://www.jooq.org/translate/
- BL3 Redux Team: They inspired me to try and make this because I saw all the changes they did and what you can do with this game.
  - Link to the hotfix: https://github.com/BLCM/bl3mods/tree/master/EpicNNG
