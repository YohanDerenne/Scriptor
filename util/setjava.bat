@echo off

@REM ===========================================================
@REM CONFIG
@REM ===========================================================
set java6=C:\usine-dev\programs\jdk\jdk-1.6.0_45
set java7=C:\usine-dev\programs\jdk\jdk-1.7.0_79
set java8=C:\usine-dev\programs\jdk\jdk-1.8.0_191
@REM set java11=C:\usine-dev\programs\jdk\jdk-11.0.18+10
set java11=C:\usine-dev\programs\jdk\jdk-11.0.20.1+1

set mvn6=C:\usine-dev\programs\maven\maven-3.0.4
set mvn7=C:\usine-dev\programs\maven\maven-3.3.1
set mvn8=C:\usine-dev\programs\maven\maven-3.6.2
set mvn11=C:\usine-dev\programs\maven\maven-3.9.4

@REM ===========================================================
@REM PARAM
@REM ===========================================================
set program=%0%
set version=%1%
set global=%2%

IF /i "%1" == "/?" ( CALL:HELP & GOTO:EOF )
IF /i "%1" == "-h" ( CALL:HELP & GOTO:EOF )
IF /i "%1" == "--help" ( CALL:HELP & GOTO:EOF )
IF /i "%2" == "-g" ( CALL:GLOBAL & GOTO:EOF )
IF /i not "%1" == "" ( CALL:LOCAL & GOTO:EOF )

@REM ===========================================================
@REM HELP
@REM ===========================================================
:HELP
	ECHO PRE-REQUIS :  
		ECHO 	La variable PATH de l'environnement Windows doit etre configure en cas de changement de la version de java sur l'ensemble du systeme (-g).
		ECHO 	Ajouter dans PATH la valeur suivante : ^%%JAVA_BIN^%%
		ECHO 	Ajouter dans PATH la valeur suivante : ^%%M2_BIN^%%
		ECHO 	(Attention au mvn se trouvant dans le repertoire de chocolatay)
	ECHO.
    ECHO SIGNATURE APPEL : %program% [version_java] [-g]
	ECHO.
    ECHO PARAMETRES : 
        ECHO    - [version_java] : Choix de la version de java parmi les valeurs suivantes : 6 / 7 / 8
        ECHO    - [-g] : Optionnel, Ajouter "-g" pour modifier la version de java sur le systeme, sinon seul le terminal actuel profitera de ce changement.
	ECHO.
	ECHO EXEMPLES : 
		ECHO 	%program% 6
		ECHO 	%program% 8 -g
    GOTO:EOF

@REM ===========================================================
@REM GLOBAL
@REM ===========================================================
:GLOBAL
	echo Modification de la version java/maven sur le system (global)...
	(
		if %version% == 6 (
			setx JAVA_BIN %java6%\bin
			setx JAVA_HOME %java6%
			setx M2_BIN %mvn6%\bin
			setx M2_HOME %mvn6%
		) else if %version% == 7 (
			setx JAVA_BIN %java7%\bin
			setx JAVA_HOME %java7%
			setx M2_BIN %mvn7%\bin
			setx M2_HOME %mvn7%
		) else if %version% == 8 (
			setx JAVA_BIN %java8%\bin
			setx JAVA_HOME %java8%
			setx M2_BIN %mvn8%\bin
			setx M2_HOME %mvn8%			
		) else if %version% == 11 (
			setx JAVA_BIN %java11%\bin
			setx JAVA_HOME %java11%
			setx M2_BIN %mvn11%\bin
			setx M2_HOME %mvn11%
		) else (
			echo La version %version% est inconnu
			GOTO:EOF
		)
	) >nul
	CALL RefreshEnv.cmd
	call mvn -v
	GOTO:EOF

@REM ===========================================================
@REM LOCAL
@REM ===========================================================
:LOCAL
	echo Modification de la version java/maven sur le terminal...
	if %version% == 6 (
		set JAVA_BIN=%java6%\bin
		set JAVA_HOME=%java6%
		set M2_BIN=%mvn6%\bin
		set M2_HOME=%mvn6%
	) else if %version% == 7 (
		set JAVA_BIN=%java7%\bin
		set JAVA_HOME=%java7%
		set M2_BIN=%mvn7%\bin
		set M2_HOME=%mvn7%
	) else if %version% == 8 (
		set JAVA_BIN=%java8%\bin
		set JAVA_HOME=%java8%
		set M2_BIN=%mvn8%\bin
		set M2_HOME=%mvn8%		
	) else if %version% == 11 (
		set JAVA_BIN=%java11%\bin
		set JAVA_HOME=%java11%
		set M2_BIN=%mvn11%\bin
		set M2_HOME=%mvn11%
	) else (
		echo La version %version% est inconnu
		GOTO:EOF
	)
	set PATH=%JAVA_BIN%;%M2_BIN%;%PATH%
	call mvn -v
	
@REM SET PATH=C:\usine-dev\programs\jdk\jdk-1.6.0_45\bin;C:\usine-dev\programs\maven\maven-3.0.4\bin;%PATH%
@REM SET M2_HOME=C:\usine-dev\programs\maven\maven-3.0.4
@REM SET JAVA_HOME=C:\usine-dev\programs\jdk\jdk-1.6.0_45

