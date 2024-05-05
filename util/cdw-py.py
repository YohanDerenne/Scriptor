import argparse
import os
import glob
import conf
import log

def main():
    # Load Config
    config = conf.load('cdw-conf.json')

    # Arg manager
    parser = argparse.ArgumentParser(description='Find and change directory to project')
    parser.add_argument(
        'projet',
        type=str,
        help='Nom du projet'
    )
    parser.add_argument(
        'composants',
        nargs="*",
        type=str,
        help='Nom des composants'
    )
    args = parser.parse_args()
    
    # Recherche du ws
    if args.projet in config.keys():
        findProjectAndStopIfExist(config[args.projet], [])
    
    # Recherche du projet/sous-projet
    for workspace in config.keys():
        pathWorkspace = config[workspace] + "\\" + args.projet
        findProjectAndStopIfExist(pathWorkspace, args.composants)
    
    # Recherche dans le dossier courant
    args.composants.insert(0, args.projet)
    findProjectAndStopIfExist(".", args.composants)

    print('Projet introuvable')
    exit(1)


def findProjectAndStopIfExist(path, sousProjets):
    if os.path.isdir(path):
        cdPath = path
        for sp in sousProjets:
            dirs = glob.glob(cdPath + "\\*" + sp)
            if len(dirs) == 1 and os.path.isdir(dirs[0]):
                cdPath = dirs[0]
            else:
                break
        if len(cdPath) > 1 :  
            print(cdPath)
            exit(0)


if __name__ == '__main__':
    main()
