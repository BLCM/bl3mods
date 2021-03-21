import sys
import subprocess
import os
from os import path
from sys import platform

# I am attempting to make it easier to install python libaries for users. I do not have a lot of experiences with other platforms with installing python libaries, so this will probable be wrong
if platform == "linux" or platform == "linux2":
    subprocess.check_call([sys.executable, 'sudo', 'pip', 'install', '--user', 'appdirs'])
    subprocess.check_call([sys.executable, 'sudo', 'pip', 'install', '--user', 'pyodbc'])
    subprocess.check_call([sys.executable, 'sudo', 'pip', 'install', '--user', 'flatten-json'])
elif platform == "mac":
    subprocess.check_call([sys.executable, 'easy_install', 'pip'])
    subprocess.check_call([sys.executable, 'pip', 'install', 'appdirs'])
    subprocess.check_call([sys.executable, 'pip', 'install', 'pyodbc'])
    subprocess.check_call([sys.executable, 'pip', 'install', 'flatten-json'])
elif platform == "win32":
    # implement pip as a subprocess:
    None
    # subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'appdirs'])
    # subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyodbc'])
    # subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flatten-json'])


found_it = ''
for r, d, f in os.walk("C:\\"): # change the hard drive, if you want
    if "flatten_json\__init__.py" in found_it:
        break
    elif "flatten_json" in r:
        found_it = r
        for file in f:
            if file == "__init__.py":
                found_it += "\\"+ file
                break

if path.isfile(found_it):
    read = open(found_it, "r")


NewLines = read.readlines()
# these are 1 less than it looks like it should be, but the program starts at 0, and not one
NewLines[42] = "    # if replace_separators is not None:\n"
NewLines[43] = "        # new_key = str(new_key).replace(separator, replace_separators)\n"
NewLines[45] = "        return u'{}.{}[{}]'.format(previous_key, previous_key, new_key)\n"

read = open(found_it, "w")
read.writelines(NewLines)
read.close()
