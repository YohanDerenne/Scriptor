import sys
import color

def warn(msg): 
    print(color.SFC_YELLOW + "WARNING: " + msg + color.RESET, file=sys.stderr)

def error(msg):
    print(color.SFC_RED + "ERROR: " + msg + color.RESET, file=sys.stderr)

