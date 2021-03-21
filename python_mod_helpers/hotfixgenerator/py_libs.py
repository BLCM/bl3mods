import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'appdirs'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyodbc'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flatten-json'])