import argparse
import conf
import run

def main():
    # Load Config
    config = conf.load('jboss-conf.json')
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch JBOSS Server')
    parser.add_argument(
        'jboss_version',
        choices=config.keys(),
        type=str,
        help='Nom du projet'
    )
    args = parser.parse_args()
    run.cmd(config[args.jboss_version])
    
if __name__ == "__main__":
    main()