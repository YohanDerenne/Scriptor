import sys
import color

def info(msg):
    print("INFO: " + msg, file=sys.stderr)

def sucess(msg):
    print(color.SFC_GREEN + "SUCESS: " + msg + color.RESET, file=sys.stderr)
    
def warn(msg): 
    print(color.SFC_YELLOW + "WARNING: " + msg + color.RESET, file=sys.stderr)

def error(msg):
    print(color.SFC_RED + "ERROR: " + msg + color.RESET, file=sys.stderr)
