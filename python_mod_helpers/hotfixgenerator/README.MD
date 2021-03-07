# DESCRIPTION

This application is a WIP tool for modders to help streamline the process of finding information and creating .bl3hotfix mods

# NOTE

I am a college student, so I will not be able to work on this all the time, but I will when I have free time.
This will me a massive passion project for me, so there will be many errors and bugs in my program, so keep in mind.
I will try and take any feedback as soon as I can, but just note that I wont respond to everything. Also no I am not working with a team, this is something I am doing all on my own

# USEAGE

Currently I do not have a .exe that you can run to manually start the program.
In order to get this working you will need a program that runs python programs.
My personal recomendation is VScode. I have created a .bat file that you can run to install all the needed libaries.

Later on hopefully you will not need external hardware to run this program, but for now you will.

## Program Caveat

The program will not work proporly even if you ran the .bat file first. This is because variables in bl3data.py, `'data_dir'` and `'ueserialize_path'`, make a unique .ini file that will be different for each user. These variables will require you to go and put in your own file location. Here are some useful resources and tips to follow.

1. 'data_dir'
   1. Follow instructions at: https://github.com/BLCM/BLCMods/wiki/Accessing-Borderlands-3-Data
   2. Once you have extracted all the data, set 'data_dir'` as the extracted_new file path.
      1. EX: F:/Users/Name/Desktop/extracted_new
2. 'ueserialize_path': Since this was confusing for me, I will give specific instructions.
   1. Download the file from here: https://github.com/apocalyptech/JohnWickParse
   2. Extract the file into a good location.
   3. Open up command line and type cd <Location/Of/Extracted/JohnWickParse>, then hit enter.
   4. Click this link and run the .exe file: https://win.rustup.rs/
   5. Once you have run that, go back you your command line and type cargo build.
      1. This may take a minute, so be patient with it.
   6. One it is done building, get the file location where the debug file is.
   7. Get that file path and set 'ueserialize_path' equal to that.
      1. EX: F:/Users/Name/Desktop/extracted_new/JohnWickParse-indexed_arrays/target/debug
3. If something went wrong with the nameing or other erros when creating it, go to this file location: C:\Users\Name\AppData\Local\bl3data\bl3data\bl3data.ini
   1. Open it and manually change the paths to the correct path.

I pull from a database I personally use, and because of that I will have to change some parts of the code to hide personal information.

In the future I wish to move to a public one where anyone can grab this information, but for right now some functionality of the code will not work.

## Exception

If you have a SQL server and know how to insert information, then you would be able to use your own tables and database to pull information from.
I have left in this folder some of the files I used to help format the SQL file I pulled from. You will also want a formatter, which there is one
I used in the credits section. If you do not then my program is still useable, just know some functionality will not be useable.

# CREDITS

I did not create most of these files, most of the hard work was already done.
I decided to make something new from projects other people have done.
List of resources that have helped me:

- apocalyptech: This program is heavly based on the research and projects
  - Github: https://github.com/apocalyptech
  - Specific reposatory I pulled from: https://github.com/BLCM/bl3mods/tree/master/python_mod_helpers
  - SQL File and Object Reference: https://apocalyptech.com/games/bl3-refs/
- Site that help format the SQL file: https://www.jooq.org/translate/
- BL3 Redux Team: They inspired me to try and make this because I saw all the changes they did and what you can do with this game.
  - Link to the hotfix: https://github.com/BLCM/bl3mods/tree/master/EpicNNG
