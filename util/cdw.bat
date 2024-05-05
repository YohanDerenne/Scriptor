@echo off
set result=
FOR /F "tokens=* USEBACKQ" %%F IN (`cdw-py %1 %2 %3 %4 %5 %6 %7`) DO (CALL SET "result=%%F")
IF %ERRORLEVEL% EQU 0 (cd %result%)