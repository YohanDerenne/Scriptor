import argparse
import os
import conf
import run
import log
import windows

def main():
    # Load Config
    config = conf.load('angular-conf.json')
    
    # Check if nvm is installed
    if run.cmdHided('nvm --version'):
        log.error("nvm n'est pas installé (introuvable)")
        exit()
        
    # Check if node is installed
    if run.cmdHided('node --version'):
        log.error("node n'est pas installé (introuvable), faire \"nvm use [version-node]\" (nvm install si besoin)")
        exit()
    
    # Check if yarn is installed
    if run.cmdHided('yarn -v'):
        log.error("yarn n'est pas installé (introuvable)")
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
    log.info("Lancement de l'IHM pour le projet " + args.project + " ")
    os.chdir(config[args.project]['path'])
    run.cmd("nvm use " + config[args.project]['node'])
    run.cmd("nvm current")
    run.cmd("yarn start")
    
if __name__ == "__main__":
    main()