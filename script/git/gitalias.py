import argparse
import configparser
import os

import log

gitConfigGlobalPath = os.path.expanduser("~") + '/.gitconfig'
gitConfigScriptorPath = os.path.dirname(__file__) + '/../../resources/.gitconfig'

def main():

    argparse.ArgumentParser(description='Inject alias in git config global file').parse_args()

    # Check files
    if not os.path.exists(gitConfigGlobalPath):
        log.error(f"Global gitconfig file '{gitConfigGlobalPath}' not found.")
        return
    
    if not os.path.exists(gitConfigScriptorPath):
        log.error(f"Scriptor gitconfile file resource '{gitConfigScriptorPath}' not found.")
        return
    
    gitConfigGlobalParser = configparser.ConfigParser()
    gitConfigGlobalParser.read(gitConfigGlobalPath)
    
    gitConfigScriptorParser = configparser.ConfigParser()
    gitConfigScriptorParser.read(gitConfigScriptorPath)

    # Merge and skip duplicate
    for section in gitConfigScriptorParser.sections():
        if not gitConfigGlobalParser.has_section(section):
            gitConfigGlobalParser.add_section(section)
        
        for key, value in gitConfigScriptorParser.items(section):
            if not gitConfigGlobalParser.has_option(section, key) or gitConfigGlobalParser.get(section, key) != value :
                gitConfigGlobalParser.set(section, key, value)
            else:
                log.info(f"Duplicate found inside section '{section}', key '{key}' : ingore it.")

    # Save file global
    with open(gitConfigGlobalPath, 'w') as configfile:
        gitConfigGlobalParser.write(configfile)

    log.sucess(f"Merge done in '{gitConfigGlobalPath}'.")

if __name__ == '__main__':
    main()
