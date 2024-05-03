import argparse
import conf
import run

def main():
    # Load Config
    config = conf.load('wiremock-conf.json')
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch Wiremock Server')
    parser.add_argument(
        'projet',
        choices=config.keys(),
        type=str,
        help='Nom du projet'
    )
    args = parser.parse_args()
    run.cmd(config[args.projet])
    
if __name__ == "__main__":
    main()