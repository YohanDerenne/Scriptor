@echo off
set error=0
set result=
FOR /F "tokens=* USEBACKQ" %%F IN (`cdw-py %1 %2 %3 %4 %5 %6 %7`) DO (
    IF %ERRORLEVEL% EQU 0 SET error=1
    CALL SET "result=%%F"
)
IF %error% == "0" (cd %result%)