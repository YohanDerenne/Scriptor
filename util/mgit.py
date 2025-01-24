import argparse
import os
import sys
import color
import conf
import log
import terminal

# Load Config
config = conf.load('mgit-conf.json')

def main():    
    # Arg manager
    parser = argparse.ArgumentParser(description="Multiple git repo manager", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'project',
        choices=config.keys(),
        type=str,
        help='Projet key to group of repo'
    )
    parser.add_argument(
        '-f',
        '--fetch',
        dest="fetch",
        action='store_true',
        help="Fetch all repo"
    )
    parser.add_argument(
        '-p',
        '--pull',
        dest="pull",
        action='store_true',
        help="Pull rebase all repo"
    )    
    parser.add_argument(
        '-c',
        '--checkout',
        dest="checkout",
        metavar='branch',
        type=str,
        help='Switch to branch in all repo'
    )
    
    # Parse Args
    args = parser.parse_args()

    if len(sys.argv) < 3:
        parser.print_help(sys.stderr)
        exit()


    for dir in config[args.project] :
        if not os.path.isdir(dir):
            log.error(f"{dir} is not a valid directory.")
            return
            
        if not os.path.isdir(os.path.join(dir, ".git")):
            log.error(f"{dir} is not a git directory.")
            return
        
        print()
        log.info("==================================================================================")
        log.info(f"Repo : {dir} -> {colorBranch(getCurrentBranch(dir))}{colorBranch(f' -> {args.checkout}' if args.checkout else '')}")
        log.info("==================================================================================")

        if args.fetch or args.pull :
            log.info("Fetching...")
            fetch = terminal.cmdOutput(f"git -C {dir} fetch --all --quiet")
            if fetch.returncode:
                log.error(terminal.getError(fetch))
            else :
                lastCommit = terminal.cmdOutput(f"git -C {dir} for-each-ref --sort=-committerdate --format=\"Last commit : %(refname:short) -> %(authorname) %(subject)\" refs/heads/ | head -n 1")
                if lastCommit.returncode:
                    log.error(terminal.getError(lastCommit))
                else :
                    log.sucess(terminal.getOutput(lastCommit))

        if args.checkout :
            log.info(f"Switching to branch {args.checkout}...")
            checkout = terminal.cmdOutput(f"git -C {dir} checkout {args.checkout}")
            if checkout.returncode:
                log.error(terminal.getError(checkout))
            else :
                log.sucess(terminal.getError(checkout))

        # TODO : Add pull rebase
        # TODO : Format output f"...{var}..."
        # TODO : Add color to branch name if master/main or dev/develop
        # TODO : Doc each function in readme
        # TODO : resumé
        # TODO : status

def colorBranch(branch):
    colorBranch = color.SFC_YELLOW if branch == "master" or branch == "main" \
        else color.SFC_GREEN if branch == "dev" or branch == "develop" \
        else color.SFC_MAGENTA
    return colorBranch + branch + color.RESET

def getCurrentBranch(dir):
    return terminal.getOutput(terminal.cmdOutput(f"git -C {dir} branch --show-current"))

if __name__ == '__main__':
    main()
