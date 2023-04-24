@ECHO OFF
chcp 65001 >NUL
SET PROJET=%1

IF /i "%1" == "/?" ( CALL:HELP & GOTO:EOF )
IF /i "%PROJET%" == "" ( CALL:GLOBAL & GOTO:EOF )
IF /i "%PROJET%" == "global" ( CALL:GLOBAL & GOTO:EOF )
IF /i "%PROJET%" == "pub" ( CALL:PUB & GOTO:EOF )
IF /i "%PROJET%" == "sdpub" ( CALL:SDPUB & GOTO:EOF )
IF /i "%PROJET%" == "selddd" ( CALL:SELDDD & GOTO:EOF )
IF /i "%PROJET%" == "cdc" ( CALL:CDC & GOTO:EOF )
IF /i "%PROJET%" == "cdc2" ( CALL:CDC2 & GOTO:EOF )
IF /i "%PROJET%" == "syliqsuivi" ( CALL:SYLIQ_SUIVI & GOTO:EOF )
IF /i "%PROJET%" == "syliqdroit" ( CALL:SYLIQ_DROIT & GOTO:EOF )
IF /i "%PROJET%" == "dril" ( CALL:DRIL & GOTO:EOF )
ECHO ERREUR: "%PROJET%" est un projet inconnu.
CALL:HELP
GOTO:EOF

@REM ===========================================================
@REM DRIL
@REM ===========================================================
:DRIL
    ECHO Lancement du WireMock DRIL...
    CD C:\usine-dev\workdir\workspace18\DRIL\drl-sapp\drl-sapp-stub\src\integration
    java -jar wiremock-standalone-2.8.0.jar -port 8083
    GOTO:EOF

@REM ===========================================================
@REM PUB
@REM ===========================================================
:PUB
    ECHO Lancement du WireMock PUB...
    CD C:\usine-dev\workdir\workspace18\PUB\portail-services-ng\src\test\webapp\WEB-INF\stub
    java -jar wiremock-standalone-2.27.2.jar --port 8081 --verbose
    GOTO:EOF
	
@REM ===========================================================
@REM SDPUB
@REM ===========================================================
:SDPUB
    ECHO Lancement du WireMock SuiviDossier Pub...
	CALL setjava 8
    CD C:\usine-dev\workdir\workspace16\PUB\suivi-dossier\suividossier-ihm\src\test\webapp\WEB-INF\stub
    CALL proxy
    GOTO:EOF

@REM ===========================================================
@REM SELDDD
@REM ===========================================================
:SELDDD
    ECHO Lancement du WireMock SELDDD Pub...
	CALL setjava 8
    CD C:\usine-dev\workdir\workspace18\SELDDD\agedepart-sapp\agedepart-sapp-ng\src\test\webapp\WEB-INF\stub
    CALL proxy
    GOTO:EOF

@REM ===========================================================
@REM SYLIQ SUIVI
@REM ===========================================================
:SYLIQ_SUIVI
    ECHO Lancement du WireMock SYLIQ SUIVI...
	CALL setjava 8
    CD C:\usine-dev\workdir\workspace16\PUB\suivi-dossier\syliq-suivi\src\test\webapp\WEB-INF\stub
    CALL run_wiremock
    GOTO:EOF

@REM ===========================================================
@REM SYLIQ DROIT
@REM ===========================================================
:SYLIQ_DROIT
    ECHO Lancement du WireMock SYLIQ DROIT...
	CALL setjava 8
    CD C:\usine-dev\workdir\workspace16\PUB\suivi-dossier\syliq-droit-client\src\test\webapp\WEB-INF\stub
    CALL run_wiremock
    GOTO:EOF
	
@REM ===========================================================
@REM CDC
@REM ===========================================================
:CDC
    ECHO Lancement du WireMock CDC...
    CD C:\usine-dev\workdir\workspace18\SAE\lib\cdc-model\src\test\stub
    java -jar wiremock-standalone-2.27.2.jar --port 8081 --verbose 
	@REM --global-response-templating
    GOTO:EOF

@REM ===========================================================
@REM CDC2
@REM ===========================================================
:CDC2
    ECHO Lancement du WireMock CDC2...
    CD C:\usine-dev\workdir\workspace18\SAE\lib\cdc-wiremock
	CALL mvn clean package assembly:single
	CD target
	java -jar cdc-wiremock-1.0.1-SNAPSHOT-jar-with-dependencies.jar
    GOTO:EOF

@REM ===========================================================
@REM GLOBAL
@REM ===========================================================
:GLOBAL
    ECHO Lancement du WireMock global...
    CD C:\usine-dev\programs\wiremock
    java -jar wiremock-jre8-standalone-2.33.2.jar --port 8001 --root-dir . --verbose
    GOTO:EOF

@REM ===========================================================
@REM HELP
@REM ===========================================================
:HELP
    ECHO Exemple d'execution : wiremock [nom_projet]
    ECHO Liste des projets : 
        ECHO    - PUB
        ECHO    - global
    GOTO:EOF