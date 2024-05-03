import argparse
import os
import conf

projects = conf.load('symfony-conf.json')

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
