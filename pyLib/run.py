import os
import re
import subprocess

def cmd(cmd, showCmd=True):
    if showCmd:
        cmdSecure = re.sub("password=[^\\s]+", 'password=*******', cmd)
        cmdSecure = re.sub("pwd=[^\\s]+", 'pwd=*******', cmdSecure)
        print('====================================================================')
        print('RUN CMD : ' + cmdSecure)
        print('====================================================================')
    return subprocess.call(cmd, shell=True)

def cmdOutput(cmd):
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)    

def cmdHided(cmd):
    return subprocess.call(cmd, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True)
