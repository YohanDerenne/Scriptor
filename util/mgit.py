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
            print(dir)
            result = terminal.cmdOutput("git -C " + dir + " fetch --all --quiet")
            error = terminal.getError(result)
            if error != "":
                log.error(terminal.getError(result))
            else :
                hashLocal = terminal.cmdOutput("git -C " + dir + " rev-parse @").stdout
                # hashRemote = terminal.cmdOutput("git -C " + dir + " rev-parse @{u}").stdout
                # hashBase = terminal.cmdOutput("git -C " + dir + " merge-base @ @{u}").stdout
                print(hashLocal)
    

if __name__ == '__main__':
    main()
