@echo off
setlocal

@rem Script path
set RUNSCRIPTPATH=%~dp0
set BOT_APP=.\wth.py

@rem Activate virtual environment
call %RUNSCRIPTPATH%\venv\Scripts\activate.bat

IF NOT EXIST %BOT_APP% (
    echo Couldn't find %BOT_APP%
    goto _EXIT
)

@rem Running bot on server using Python
python %BOT_APP%

endlocal

:_EXIT