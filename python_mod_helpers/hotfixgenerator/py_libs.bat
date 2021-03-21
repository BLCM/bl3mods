@echo off
start pip install appdirs & pip install pyodbc & pip install flatten-json
pause
REM Once you have run this bat file, please follow these instructions.
REM I have modified the flatten-json libary that you are supposed to have.
REM this wil slightly vary for users, here is an example of what yours might be: C:\Users\<Name>\AppData\Local\Programs\Python\Python39\Lib\site-packages\flatten_json
REM Open the __init__.py file, comment out lines 44-45. On line 46 change the elif to just an if.
REM On line 48, comment that that line out. Hit Enter and place this inside: return u"{}.{}[{}]".format(previous_key, previous_key, new_key)
REM I will work on make so this porcess is automatic, but for now the you will need to do this manually.