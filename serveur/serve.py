import argparse
import os
import json

configPath = os.path.dirname(__file__) + '/../config/symfony-conf.json'
with open(configPath, 'r') as f:
    config = json.load(f)
projects = config

cmd = 'symfony serve'

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

    print("===============================")
    print(args.project)
    print(projects[args.project])
    print("===============================")
    os.chdir(projects[args.project])
    os.system(cmd)

if __name__ == "__main__":
    main()
