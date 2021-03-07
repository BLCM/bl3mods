# DESCRIPTION

This application is a WIP tool for modders to help streamline the process of finding information and creating .bl3hotfix mods

# NOTE

I am a college student, so I will not be able to work on this all the time, but I will when I have free time.
This will me a massive passion project for me, so there will be many errors and bugs in my program, so keep in mind.
I will try and take any feedback as soon as I can, but just note that I wont respond to everything. Also no I am not working with a team, this is something I am doing all on my own

# USEAGE

Currently I do not have a .exe that magically runs everything you need and makes it work perfectly.

In order to get this tool working, you will need a program that runs Python programs.

My personal recomendation is VScode, and install the Python extention. However any program that runsPython scrips should work fine.

You will need to install Python on your computer. Link: https://www.python.org/downloads/

I have created a .bat file that you can run to install all the needed python libaries.

## Tool Caveats

The program will not work proporly even if you have python and ran the .bat file.

This is because variables in bl3data.py, `'data_dir'`, `'ueserialize_path'`, and the database functions will be unique for each person.

In the future I wish to solve the database issue by making a public one, but for the other variables you will have to do that on your own.

## Instructions

Instructions for fixing the caveats and to fully utilize the program

1. 'data_dir'
   1. Follow instructions at: https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data
   2. Once you have extracted all the data, set 'data_dir'` as the extracted_new file path.
      1. EX: ''F:/Users/Name/Desktop/extracted_new''
2. 'ueserialize_path': Since this was confusing for me, I will give specific instructions to help people.
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
3. Data Base connections.
   1. In bl3data.py, I have modified the code to use `pyodbc` connections instead of what it normally is.
   2. If you have a SQL server (SQLEXPRESS for example) and know how to insert information, then you would be able to use your own tables and database to pull information from.
      1. This is what I have done, as I already had it  and I wanted to test to see if it would work.
      2. You may change the code section to whatever suits you, but this is what I have personally done.
   3. You will need apocalyptech MariaDB datadump, Link is in the Credits.
      1. I have left in this folder some of the files I used to help format the SQL file I used.
      2. **NOTE**: I did not comment my formatter files well. Reason being that it was a mach program I made to ease my pain. You will more than likely encounter erros, but I beleive in you.
   4. You will also want a SQL formatter. Link also in the Credits.
   5. If you do not want to make your own database and deal with all the hassle, Then this Program is still very useful, but some of the functionality will not work.

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
