@ECHO OFF
SET COMMON_DIR=C:\usine-dev\workdir\workspace18\
IF /i "%1" == "" (
	CD %COMMON_DIR%
) ELSE (
	IF /i "%2" == "" (
		CD %COMMON_DIR%\%1
	) ELSE (
		CD %COMMON_DIR%\%1\\*%2
	)
)
