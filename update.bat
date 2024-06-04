@echo off

set curdir=%~dp0
set pyPath=%curdir%\pyLib
set configPath=%curdir%\config
set configPathTemplate=%curdir%\config-template
set resourcesPath=%curdir%\resources

@REM ===========================================================
@REM Check if Python is installed
@REM ===========================================================

echo Checking Python installed...
python --version 2>NUL
if errorlevel 1 goto errorNoPython
goto addPythonPath

:errorNoPython
    echo Error^: Python not installed
    goto :EOF

@REM ===========================================================
@REM Add PYTHONPATH if not set
@REM ===========================================================

:addPythonPath
    echo Adding PYTHONPATH env variable (%pyPath%)...
    setx PYTHONPATH %pyPath%

@REM ===========================================================
@REM Associate .py file to be run by python.exe
@REM ===========================================================
set "extpy=.py"
setlocal enabledelayedexpansion
if "!pathext:%extpy%;=!"=="!pathext!" (
    endlocal
    echo Associate .py file to be run by python.exe...
    setx PATHEXT %PATHEXT%;.py;
)
endlocal

@REM ===========================================================
@REM Add All folder to PATH if not set
@REM ===========================================================

@REM Get PATH of user
FOR /F "tokens=*" %%g IN ('powershell -NoProfile -Command "(Get-ItemProperty HKCU:\Environment).PATH"') do (SET newPath=%%g)
set initialPath=%newPath%;
set newPath=%newPath%;

@REM Add script dir to PATH
CALL:ADD_FOLDER_TO_PATH %curdir%

@REM For each folder
for /d %%i in (%curdir%\*) do (
    call:ADD_FOLDER_TO_PATH "%%i"
)

@REM Save path
if not "%newPath%" == "%initialPath%" (
    echo Updating PATH...
    setx Path "%newPath%"
)

@REM ===========================================================
@REM END
@REM ===========================================================
echo /!\ Restart terminal /!\
goto:EOF

@REM ===========================================================
@REM Add Directory to PATH
@REM ===========================================================
:ADD_FOLDER_TO_PATH
    set folderPath=%~1
    setlocal enabledelayedexpansion
    if NOT "%folderPath%" == "%pyPath%" if NOT "%folderPath%" == "%pyPath%" if NOT "%folderPath%" == "%configPath%" if NOT "%folderPath%" == "%configPathTemplate%" if NOT "%folderPath%" == "%resourcesPath%" IF NOT "%folderPath%" == "" if "!newPath:%folderPath%;=!"=="!newPath!" (
        endlocal
        echo Adding %folderPath% to PATH...
        set newPath=%newPath%%folderPath%;
    )
    endlocal
