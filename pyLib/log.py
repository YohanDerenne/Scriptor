import color

def warn(msg): 
    print(color.COLOR_SFC_YELLOW + "WARNING: " + msg + color.COLOR_RESET)

def error(msg):
    print(color.COLOR_SFC_RED + "ERROR: " + msg + color.COLOR_RESET)

