@echo off
set result=
FOR /F "tokens=* USEBACKQ" %%F IN (`cdw-py %1 %2 %3 %4 %5 %6 %7`) DO (
    CALL SET "result=%%F"
)
CALL SET "cmd=cd %result%"
IF "%cmd%" NEQ "cd " CALL %cmd%