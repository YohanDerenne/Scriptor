import argparse
import os
import json

configPath = os.path.dirname(__file__) + '/../config/symfony-conf.json'
with open(configPath, 'r') as f:
    config = json.load(f)
projects = config

cmd = 'npm run watch'

def main():   
    parser = argparse.ArgumentParser(
        description='Run \"' + cmd + '\" on a project'
    )
    
    parser.add_argument(
        'project',
        choices=projects.keys(),
        type=str, 
        help='Project name'
    )
    args = parser.parse_args()

    if args.project in projects :
        print("===============================")
        print(args.project)
        print(projects[args.project])
        print("===============================")
        os.chdir(projects[args.project])
        os.system(cmd)
    else :
        print("Project \"" + args.project + "\" is unknow")

if __name__ == "__main__":
    main()
