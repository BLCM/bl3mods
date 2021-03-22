@echo off

python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
echo Now opeing the download URL.

echo %os% | find "Windows"> nul || goto linux
echo Hit Enter to download the appropiate version of python 
pause 
start "" http://www.stackoverflow.com
:linux
echo %os% | find "Linux"> nul || goto mac
:mac
echo %os% | find "Mac"> nul

:PYTHON_DOES_EXIST
:: This will retrieve Python 3.8.0 for example.
for /f "delims=" %%V in ('python -V') do @set ver=%%V
python py_libs.py




@REM :: Check for Python Installation
@REM python --version 3>NUL

@REM if errorlevel 1 
@REM goto errorNoPython

@REM :: Reaching here means Python is installed.
@REM :: Execute stuff...
@REM python py_libs.py
@REM :: Once done, exit the batch file -- skips executing the errorNoPython section
@REM goto:eof

@REM :errorNoPython
@REM echo.
@REM echo Error^: Python not installed
@REM "C:\Program Files\used\systems\innoventiq\accumanager\required\excutables\python-3.7.3-amd64.exe"