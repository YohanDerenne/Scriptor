import sys
import color

config = {
    "ERROR": {
        "LEVEL" : "ERROR",
        "COLOR" : color.SFC_RED
    },
    "SUCCESS": {
        "LEVEL" : "SUCCESS",
        "COLOR" : color.SFC_GREEN
    },
    "INFO": {
        "LEVEL" : "INFO",
        "COLOR" : color.SFC_BLUE
    },
    "WARNING": {
        "LEVEL" : "WARNING",
        "COLOR" : color.SFC_YELLOW
    },
    "DEBUG": {
        "LEVEL" : "DEBUG",
        "COLOR" : color.SFC_GREY
    },
}

def __logger(configLevel, msg):
    print("[" + configLevel["COLOR"] + configLevel["LEVEL"] + color.RESET + "] " + msg, file=sys.stderr)
    
def info(msg):
    __logger(config["INFO"], msg)

def sucess(msg):
    __logger(config["SUCCESS"], msg)
    
def warn(msg): 
    __logger(config["WARNING"], msg)

def error(msg):
    __logger(config["ERROR"], msg)

def debug(msg):
    __logger(config["DEBUG"], msg)