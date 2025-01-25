import os
import re
import log

ignoreFilesInDirectories = [
    ".git",
    "resources",
    "config"
    "config-template",
    "lib",
]

ignoreFileNameKeys = [
    "-py.py",
    "set_colors.bat"
]

validFileNameKeys = [
    ".py",
    ".bat",
    ".sh"
]

def main():
    scripts = getListScriptsName()    
    log.info("Available commands:\n")
    for script in scripts:
        print(script)
    print("")
    log.info("TOTAL : " + str(len(scripts)))
        
def getListScriptsName():
    scripts = []
    scriptorPath = os.path.dirname(__file__) + '/../'
    for path, subdirs, fileNames in os.walk(scriptorPath):
        if isIgnorableDirectory(path) :
            continue
        for fileName in fileNames:
            if isNotIgnorableFile(fileName):
                scripts.append(re.sub(r"\..*", '', fileName))
    scripts.sort()
    return scripts

def isIgnorableDirectory(dir):
    return any(blackListDirectory in dir for blackListDirectory in ignoreFilesInDirectories)

def isNotIgnorableFile(file):
    return not any(key in file for key in ignoreFileNameKeys) and any(key in file for key in validFileNameKeys)

if __name__ == '__main__':
    main()