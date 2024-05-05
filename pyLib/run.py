import os
import re
import subprocess

def cmd(cmd):
    print('====================================================================')
    print('RUN CMD : ' + re.sub("password=[^\\s]+", 'password=*******', cmd))
    print('====================================================================')
    return subprocess.call(cmd, shell=True)

def cmdOutput(cmd):
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)    

def cmdHided(cmd):
    try:
        return subprocess.call(cmd, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT, shell=True)
    except FileNotFoundError:
        print('error')
        return 1