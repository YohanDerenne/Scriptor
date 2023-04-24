@ECHO OFF
chcp 65001 >NUL

@REM ===========================================================
@REM CONFIG
@REM ===========================================================
SET NODE_VERSION_DAAH=14.20
SET PATH_DAAH=C:\usine-dev\workdir\workspace18\DAAH\daah-sapp\daah-sapp-ui

SET NODE_VERSION_PUB=10.7.0
SET PATH_PUB=C:\usine-dev\workdir\workspace18\PUB\portail-services-ng

SET NODE_VERSION_SDDD=14.20.1
SET PATH_SDDD=C:\usine-dev\workdir\workspace18\SELDDD\agedepart-sapp\agedepart-sapp-ng

SET NODE_VERSION_DRIL=16.13.1
SET PATH_DRIL=C:\usine-dev\workdir\workspace18\DRIL\drl-sapp\drl-sapp-ui

SET NODE_VERSION_DRP=18.18.0
SET PATH_DRP=C:\usine-dev\workdir\workspace\DRP\drp-sapp\drp-sapp-angular

SET PROJET_IHM=%1

@REM ===========================================================
@REM OPTIONS
@REM ===========================================================
IF /i "%1" == "daah" ( CALL:LAUNCH_DAAH & GOTO:EOF )
IF /i "%1" == "pub" ( CALL:LAUNCH_PUB & GOTO:EOF )
IF /i "%1" == "sddd" ( CALL:SDDD & GOTO:EOF )
IF /i "%1" == "dril" ( CALL:DRIL & GOTO:EOF )
IF /i "%1" == "drp" ( CALL:DRP & GOTO:EOF )
IF /i "%1" == "/?" ( CALL:HELP & GOTO:EOF )
ECHO ERREUR : "%PROJET_IHM%" est un projet inconnu.
CALL:HELP
GOTO:EOF

@REM ===========================================================
@REM DRP
@REM ===========================================================
:DRP
    ECHO Lancement de l'IHM de DRP...
    @REM ECHO ATTENTION: Le wiremock de DRIL doit être lancé.
    CD %PATH_DRP%
    ECHO Changement de la version de node vers %NODE_VERSION_DRP%
    CALL nvm use %NODE_VERSION_DRP% 
    nvm -v
    CALL yarn start
    GOTO:EOF

@REM ===========================================================
@REM DRIL
@REM ===========================================================
:DRIL
    ECHO Lancement de l'IHM de DRIL...
    ECHO ATTENTION: Le wiremock de DRIL doit être lancé.
    CD %PATH_DRIL%
    ECHO Changement de la version de node vers %NODE_VERSION_DRIL%
    CALL nvm use %NODE_VERSION_DRIL% >NUL
    nvm -v
    CALL yarn start
    GOTO:EOF

@REM ===========================================================
@REM DAAH
@REM ===========================================================
:LAUNCH_DAAH
	echo not coded
	GOTO:EOF
    ECHO Lancement de l'IHM de DAAH...
    CD %PATH_DAAH%
    ECHO Changement de la version de node vers %NODE_VERSION_DAAH%
    CALL nodist %NODE_VERSION_DAAH% 
	CALL nodist npm match 
    CALL npm start
    GOTO:EOF

@REM ===========================================================
@REM PUB
@REM ===========================================================
:LAUNCH_PUB
    ECHO Lancement de l'IHM du PUB...
    ECHO ATTENTION: Le wiremock du PUB doit être lancé.
    CD %PATH_PUB%
    ECHO Changement de la version de node vers %NODE_VERSION_PUB%
    CALL nvm use %NODE_VERSION_PUB% >NUL
    CALL npm start
    GOTO:EOF

@REM ===========================================================
@REM SDDD
@REM ===========================================================
:SDDD
    ECHO Lancement de l'IHM de SelDDD...
    ECHO ATTENTION: Le wiremock du SelDDD doit être lancé.
    CD %PATH_SDDD%
    ECHO Changement de la version de node vers %NODE_VERSION_SDDD%
    CALL nvm use %NODE_VERSION_SDDD% >NUL
    nvm -v
    CALL yarn start
    GOTO:EOF

@REM ===========================================================
@REM HELP
@REM ===========================================================
:HELP
    ECHO Exemple d'execution : ihm [nom_projet]
    ECHO Liste des projets : 
        ECHO    - DAAH
        ECHO    - PUB
    GOTO:EOF