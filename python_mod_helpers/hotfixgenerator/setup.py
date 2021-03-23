from distutils.core import setup
import py2exe
import os
from bl3data import BL3Data
from bl3hotfixmod import Mod
from _global_lists import Mod_Header, Reg_hotfix, Table_Hotfix, Mesh_Hotfix, DataBase_Results, Queue_Order, Comment_Queue, Headers_Queue, Map_Locations, Patch_Types, FileNames, File_Results_List, Search_List, ListBoxWindow
from __info_function__ import FileChoice, openBL3Hotfixfile
from __hotfix_control import Create_HotFix_File
from flatten_json import flatten
################################################################################################################################################################
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk, Frame, Button, Text, Entry, Scrollbar, END, RAISED, Label, OptionMenu, StringVar, LEFT, BOTH, RIGHT, TOP, Y, BOTTOM, DISABLED
################################################################################################################################################################
setup(windows=['__interface__.py'])