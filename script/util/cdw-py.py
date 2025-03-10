import argparse
import json
import os
import glob
import sys
import conf
import log
import string_util

def main():
    # Load Config
    config = conf.load('cdw-conf.json')

    # Arg manager
    parser = argparse.ArgumentParser(
        description='Find and change directory to project.\nWorkspaces :\n ' + string_util.dictionnaryToString(config),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'composants',
        nargs="*",
        type=str,
        help='Nom des composants'
    )
    
    # Help
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        parser.print_help(sys.stderr)
        exit()
        
    # Parse args
    args = parser.parse_args()
    
    # Recherche du ws
    if len(args.composants) == 1 and args.composants[0] in config.keys():
        cdPath = config[args.composants[0]]
        log.info("Change directory to " + cdPath)
        print(cdPath)
        exit()
        
    # Recherche du projet
    for workspace in config.keys():
        pathWorkspace = config[workspace]
        findProjectAndStopIfExist(pathWorkspace, args.composants)
    
    # Recherche dans le dossier courant
    findProjectAndStopIfExist(".", args.composants)

    log.error('Projet introuvable')
    exit(1)

def findProjectAndStopIfExist(path, sousProjets):
    cdPath = path
    if os.path.isdir(path):   
        for sp in sousProjets:
            dirs = glob.glob(cdPath + "\\*" + sp)
            if len(dirs) == 1 and os.path.isdir(dirs[0]):
                cdPath = dirs[0]
            else:
                dirs = glob.glob(cdPath + "\\" + sp + "*")
                if len(dirs) == 1 and os.path.isdir(dirs[0]):
                    cdPath = dirs[0]
                else:
                    break
        if len(cdPath) > 1 and path != cdPath:
            log.info("Change directory to " + cdPath)
            print(cdPath)
            exit(0)

if __name__ == '__main__':
    main()
