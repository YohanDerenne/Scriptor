import argparse
import conf
import terminal

def main():
    # Load Config
    config = conf.load('jboss-conf.json')
    
    # Arg manager
    parser = argparse.ArgumentParser(description='Launch JBOSS Server')
    parser.add_argument(
        'jboss_version',
        choices=config.keys(),
        type=str,
        help='Version de JBoss'
    )
    args = parser.parse_args()
    terminal.cmd(config[args.jboss_version])
    
if __name__ == "__main__":
    main()