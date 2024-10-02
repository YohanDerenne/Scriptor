import os
import re
import subprocess
import sys
import log

def cmd(cmd, showCmd=True):
    if showCmd:
        cmdSecure = re.sub("password=[^\\s]+", 'password=*******', cmd)
        cmdSecure = re.sub("pwd=[^\\s]+", 'pwd=*******', cmdSecure)
        log.info(cmdSecure)
    try:
        return subprocess.call(cmd, shell=True, stdin=sys.stdin, stdout=sys.stdout)
    except KeyboardInterrupt:
        log.error("KeyboardInterrupt")
        return 1

def cmdOutput(cmd):
    return subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)    

def cmdHided(cmd):
    return subprocess.call(cmd, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True)

def getError(result) -> str :
    if result.stderr:
        return result.stderr.decode('utf-8')[:-1]
    return ""

def getOutput(result) -> str :
    if result.stdout:
        return result.stdout.decode('utf-8')[:-1]
    return ""