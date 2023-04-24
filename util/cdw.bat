@echo off
@REM set result=
@REM FOR /F "tokens=* USEBACKQ" %%F IN (`cdw-py %1`) DO (CALL SET "result=%%F")
@REM ECHO %ERRORLEVEL%
@REM IF %ERRORLEVEL% EQU 0 (echo success && cd %result%) ELSE (echo failed && %result%)

@REM Execute python, get output and exit code
set tempFileName=C:\scripts\util\tempRes.txt
cdw-py %* > %tempFileName%
set /p result=<%tempFileName%
set erreur=%ERRORLEVEL%
del %tempFileName%

@REM echo %result%
IF %erreur% EQU 0 (cd %result%) ELSE (echo %result%)