import argparse
import os
import sys
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
        log.info(f"Repo : {dir}")

        if args.fetch :
            log.info("Fetching...")
            result = terminal.cmdOutput(f"git -C {dir} fetch --all --quiet")
            error = terminal.getError(result)
            if error != "":
                log.error(terminal.getError(result))
            else :
                res = terminal.cmdOutput(f"git -C {dir} for-each-ref --sort=-committerdate --format=\"[%(refname:short)-%(authorname)] %(subject)\" refs/heads/ | head -n 1")
                if error != "":
                    log.error(terminal.getError(res))
                else :
                    log.sucess(f"Last commit : {terminal.getOutput(res)}")


        if args.checkout :
            log.info(f"Switching to branch {args.checkout}...")
            result = terminal.cmdOutput(f"git -C {dir} checkout {args.checkout}")
            error = terminal.getError(result)
            if error != "":
                log.error(terminal.getError(result))
            else :
                res = terminal.cmdOutput(f"git -C {dir} log -1 --pretty=format:\"%h %an - %s\"")
                if error != "":
                    log.error(terminal.getError(res))
                else :
                    log.sucess(f"Switch to {args.checkout} : {terminal.getOutput(res)}")

        # TODO : Add pull rebase
        # TODO : Format output f"...{var}..."
        # TODO : Add color to branch name if master/main or dev/develop

if __name__ == '__main__':
    main()
