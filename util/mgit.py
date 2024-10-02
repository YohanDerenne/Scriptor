import argparse
import conf
import log
import terminal

# Load Config
config = conf.load('mgit-conf.json')

def main():    
    # Arg manager
    parser = argparse.ArgumentParser(description="Multiple git repo manager", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-f',
        '--fetch',
        dest="fetch",
        action='store_true',
        help="Fetch all repo"
    )
    parser.add_argument(
        'project',
        choices=config.keys(),
        type=str,
        help='Projet key to group of repo'
    )
    
    # Parse Args
    args = parser.parse_args()

    if args.fetch :
        print("fetching...")
        for dir in config[args.project] :
            result = terminal.cmdOutput("git -C " + dir + " fetch")
            error = terminal.getError(result)
            if error != "":
                log.error(terminal.getError(result))

    # if exitCode > 0:
    #     log.error("La cmd a échoué")
    

if __name__ == '__main__':
    main()
