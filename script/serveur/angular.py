import argparse
import os
import conf
import terminal
import log

def main():
    # Load Config
    config = conf.load('angular-conf.json')
    
    # Check if nvm is installed
    if terminal.cmdHided('volta -v'):
        log.error("volta n'est pas installé (introuvable)")
        exit()
        
    # Check if node is installed
    if terminal.cmdHided('node --version'):
        log.error("node n'est pas installé (introuvable), faire \"volta install node@[version-node]\"")
        exit()
    
    # Check if yarn is installed
    if terminal.cmdHided('yarn -v'):
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
    log.info("Lancement de l'IHM pour le projet " + args.project)
    os.chdir(config[args.project]['path'])
    terminal.cmd("volta install node@" + config[args.project]['node'])
    terminal.cmd("yarn start")
    
if __name__ == "__main__":
    main()