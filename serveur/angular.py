import argparse
import os
import conf
import run
import log

def main():
    # Load Config
    config = conf.load('angular-conf.json')
    
    # Check if nvm is installed
    if run.cmdHided('nvm --version'):
        log.error("nvm n'est pas installé")
        exit()
    
    # Check if yarn is installed
    if run.cmdHided('yarn -v'):
        log.error("yarn n'est pas installé")
        exit()
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch angular server')
    parser.add_argument(
        'project',
        choices=config.keys(),
        type=str,
        help='Nom du projet'
    )
    args = parser.parse_args()
    
    # Run
    print("Lancement de l'IHM pour le projet " + args.project + " ")
    os.chdir(config[args.project]['path'])
    run.cmd("nvm use " + config[args.project]['node'])
    run.cmd("nvm current")
    run.cmd("yarn start")
    
if __name__ == "__main__":
    main()