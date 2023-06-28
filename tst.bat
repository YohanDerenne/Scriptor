@echo off


for /f "tokens=1,2 delims==" %%A in ('print2') do if "%%A"=="&FN" set FN=%%B
echo %FN%