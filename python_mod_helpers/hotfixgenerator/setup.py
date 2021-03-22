from distutils.core import setup
import py2exe
import os
from bl3data import BL3Data
from __info_function__ import FileChoice, openBL3Hotfixfile
from __hotfix_control import Create_HotFix_File
from _global_lists import *
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import *
from bl3data import BL3Data
from _global_lists import *
################################################################################################################################################################
from flatten_json import flatten

setup(windows=['__interface__.py'])