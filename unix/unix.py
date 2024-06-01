import argparse
import os
import conf

projects = conf.load('unix-conf.json')

def main():   
    parser = argparse.ArgumentParser(
        description='Run wsl cmd inside directory of project'
    )
    parser.add_argument(
        'project',
        choices=projects.keys(),
        type=str,
        help='Project name'
    )
    args = parser.parse_args()
    os.system("wsl --cd " + projects[args.project])

if __name__ == "__main__":
    main()
