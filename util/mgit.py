import argparse
import os
import color
import conf
import log
import terminal

# Load Config
config = conf.load('mgit-conf.json')
    
hasWarning = False
hasError = False

def main():    
    global hasWarning
    global hasError

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
    parser.add_argument(
        '-l',
        '--log',
        dest="log",
        action='store_true',
        help="Log last commits in all repo"
    )
    
    # Parse Args
    args = parser.parse_args()

    for dir in config[args.project] :
        if not os.path.isdir(dir):
            log.error(f"{dir} is not a valid directory.")
            return
            
        if not os.path.isdir(os.path.join(dir, ".git")):
            log.error(f"{dir} is not a git directory.")
            return
        
        print()
        initialBranch = getCurrentBranch(dir);
        targetBranch = args.checkout if args.checkout and checkIfBranchExist(dir, args.checkout) else initialBranch

        infoCheckoutBranch = f'-> {colorBranch(dir, args.checkout)} ' if args.checkout else ''
        log.info("==================================================================================")
        log.info(f"Repo : {dir} -> {colorBranch(dir, initialBranch)} {infoChanges(dir)}{infoCheckoutBranch}{infoBehind(dir, targetBranch)}{infoAhead(dir, targetBranch)}")
        log.info("==================================================================================")

        if args.fetch or args.pull :
            log.info("Fetching...")
            fetch = terminal.cmdOutput(f"git -C {dir} fetch --all --quiet")
            if fetch.returncode:
                hasError = True
                log.error(terminal.getError(fetch))
            else :
                lastCommit = terminal.cmdOutput(f"git -C {dir} for-each-ref --sort=-committerdate --format=\"Last commit : %(refname:short) -> %(authorname) %(subject)\" refs/heads/ | head -n 1")
                if lastCommit.returncode:
                    hasError = True
                    log.error(terminal.getError(lastCommit))
                else :
                    log.sucess(terminal.getOutput(lastCommit))

        if args.checkout :
            log.info(f"Switching to branch {colorBranch(dir, args.checkout)}...")
            checkout = terminal.cmdOutput(f"git -C {dir} checkout {args.checkout}")
            if checkout.returncode:
                hasError = True
                log.error(terminal.getError(checkout))
            else :
                log.sucess(terminal.getError(checkout))

        if args.pull :
            log.info(f"Rebasing to current branch...")
            result = terminal.cmdOutput(f"git -C {dir} rebase origin/{targetBranch}")
            if result.returncode:
                hasError = True
                log.error(terminal.getError(result))
            else :
                log.sucess(terminal.getError(result))
        
        finalBranch = getCurrentBranch(dir);
        log.info(getRepoName(dir) + " -> " + colorBranch(dir, finalBranch) + " " + infoChanges(dir) + infoBehind(dir, finalBranch) + infoAhead(dir, finalBranch))

        # TODO : Add pull rebase
        # TODO : Format output f"...{var}..."
        # TODO : Add color to branch name if master/main or dev/develop
        # TODO : Doc each function in readme
        # TODO : resumé
    

    print()
    if hasError :
        log.error("Some errors occured.")
    elif hasWarning :
        log.warn("Some repo may be not up to date.")
    else :
        log.sucess("All repo are up to date.")


def infoChanges(dir):
    nbChanges = terminal.getOutput(terminal.cmdOutput(f"git -C {dir} status --porcelain | wc -l"))
    if nbChanges != '0' :
        setWarning()
        return f'{color.SFC_YELLOW}~{nbChanges}{color.RESET} '
    else :
        return ''

def infoBehind(dir, branch):
    nbBehind = terminal.getOutput(terminal.cmdOutput(f"git -C {dir} rev-list {branch}..origin/{branch} --count"))
    if (nbBehind != '0' and nbBehind != '') :
        setWarning()
        return f'{color.SFC_YELLOW}↓{nbBehind}{color.RESET} '
    else :
        return ''

def infoAhead(dir, branch):
    nbAhead = terminal.getOutput(terminal.cmdOutput(f"git -C {dir} rev-list origin/{branch}..{branch} --count"))
    if (nbAhead != '0' and nbAhead != '') :
        setWarning()
        return f'{color.SFC_YELLOW}↑{nbAhead}{color.RESET} '
    else :
        return ''
    
def setWarning():
    global hasWarning
    hasWarning = True

def getRepoName(dir):
    return terminal.getOutput(terminal.cmdOutput(f"git -C {dir} rev-parse --show-toplevel | awk -F'/' '{{print $NF}}'"))

def checkIfBranchExist(dir, branch):
    return terminal.cmdOutput(f"git -C {dir} rev-parse --verify {branch}").returncode == 0

def colorBranch(dir, branch):
    colorBranch = color.SFC_YELLOW if branch == "master" or branch == "main" \
        else color.SFC_GREEN if branch == "dev" or branch == "develop" \
        else color.SFC_RED if not checkIfBranchExist(dir, branch) \
        else color.SFC_MAGENTA
    return colorBranch + branch + color.RESET

def getCurrentBranch(dir):
    return terminal.getOutput(terminal.cmdOutput(f"git -C {dir} branch --show-current"))

if __name__ == '__main__':
    main()
