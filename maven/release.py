import argparse
import os
import re
import conf

config = conf.load('release-conf.json')

loginGit = config['git.login']
passwordGit = config['git.password']

args = None
complement = ''

def main():
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

    args = parser.parse_args()
    if args.complement is not None:
        complement = args.complement
    phasesArgMap[args.phase]()
        
def prepare():
    exitCode = runCmd("mvn release:prepare -DpreparationGoals=\"clean verify\" -Dusername=" + loginGit + " -Dpassword=" + passwordGit + " " + complement)
    if exitCode != 0:
        reset()
    return exitCode

def perform():
    exitCode = runCmd("mvn release:perform -Dgoals=\"deploy\" " + complement)
    if exitCode != 0:
        reset()
    return exitCode

def master():
    runCmd("git checkout develop && git pull --rebase && git checkout master && git pull --rebase && git merge develop --ff-only && git push && git checkout develop")

def reset():
    runCmd("git clean -f && git reset --hard origin/develop")
        
def all():    
    if prepare() != 0 : return
    if perform() != 0 : return
    master()    
    
def runCmd(cmd):
    print('====================================================================')
    print('RUN CMD : ' + re.sub("password=[^\\s]+", 'password=*******', cmd))
    print('====================================================================')
    return os.system(cmd)
    
if __name__ == "__main__":
    main()