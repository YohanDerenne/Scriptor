import os
import re

ignoreFilesInDirectories = [
    ".git",
    "resources",
    "config"
    "config-template",
    "pyLib",
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
    print("Available scripts (" + str(len(scripts)) + "):\n")
    for script in scripts:
        print(script)
        
def getListScriptsName():
    scripts = []
    scriptorPath = os.path.dirname(__file__)
    for path, subdirs, fileNames in os.walk(scriptorPath):
        if isIgnorableDirectory(path) :
            continue
        for fileName in fileNames:
            if isNotIgnorableFile(fileName):
                scripts.append(re.sub("\..*", '', fileName))
    scripts.sort()
    return scripts

def isIgnorableDirectory(dir):
    return any(blackListDirectory in dir for blackListDirectory in ignoreFilesInDirectories)

def isNotIgnorableFile(file):
    return not any(key in file for key in ignoreFileNameKeys) and any(key in file for key in validFileNameKeys)

if __name__ == '__main__':
    main()