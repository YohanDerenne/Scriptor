import argparse
import os

projects = {
    "LBTF" : "C:\dev\project\laboutiquefrancaise",
    "RACE" : "C:\dev\project\\race-event-app"
}

def main():   
    parser = argparse.ArgumentParser(description='Run symfony serve on a project')
    parser.add_argument('project', metavar='project', type=str, help='Project name')
    args = parser.parse_args()

    if args.project in projects :
        print("===============================")
        print(args.project)
        print(projects[args.project])
        print("===============================")
        os.chdir(projects[args.project])
        os.system('symfony serve')
    else :
        print("Project \"" + args.project + "\" is unknow")

if __name__ == "__main__":
    main()
