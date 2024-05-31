import argparse
import run
import conf

config = conf.load('release-conf.json')

loginGit = config['git.login']
passwordGit = config['git.password']

args = None
complement = ''

def main():
    global args
    global complement
    phasesArgMap = {
        'prep': prepare,
        'perf': perform,
        'reset': reset,
        'master': master,
        'all': all
    }
    
    parser = argparse.ArgumentParser(description='Outil pour les releases maven')
    parser.add_argument(
        'phase',
        choices=phasesArgMap.keys(),
        type=str,
        help='Phase de la release'
    )
    parser.add_argument(
        'complement',
        nargs='?',
        default='',
        type=str,
        help='Complément à rajouter dans les commandes exécutés'
    )
    parser.add_argument(
        '-sd',
        '--skip-doc',
        dest="skipDoc",
        action='store_true',
        help="Skip doc (-Dmaven.javadoc.skip=true)"
    )
    parser.add_argument(
        '-ss',
        '--skip-site',
        dest="skipSite",
        action='store_true',
        help="Skip site (-Dmaven.site.skip^=true)"
    )

    args = parser.parse_args()
    if args.complement is not None:
        complement = args.complement
    phasesArgMap[args.phase]()
        
def prepare():
    exitCode = run.cmd("mvn release:prepare -DpreparationGoals=\"clean verify" + getOptions() + "\" -Dusername=" + loginGit + " -Dpassword=" + passwordGit + " " + getOptions() + " " + complement)
    if exitCode != 0:
        reset()
    return exitCode

def perform():
    exitCode = run.cmd("mvn release:perform -Dgoals=\"deploy " + getOptions() + "\" " + getOptions() + " " + complement)
    if exitCode != 0:
        reset()
    return exitCode

def master():
    run.cmd("git checkout develop && git pull --rebase && git checkout master && git pull --rebase && git merge develop --ff-only && git push && git checkout develop")

def reset():
    run.cmd("git clean -f && git reset --hard origin/develop")
        
def all():
    if prepare() != 0 : return
    if perform() != 0 : return
    master()

def getOptions():
    return " -Dmaven.javadoc.skip=true" if args.skipDoc else "" + " -Dmaven.site.skip^=true" if args.skipSite else ""
    
if __name__ == "__main__":
    main()