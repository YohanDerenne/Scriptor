@echo off
for /f "delims=" %%i in ('jvm-py.py %1 %2') do %%i