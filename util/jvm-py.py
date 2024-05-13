import argparse
import conf
import windows
import log
import sys

# Load Config
config = conf.load('jvm-conf.json')

def main():    
    # Arg manager
    parser = argparse.ArgumentParser(description="Java Version Manager", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'version',
        choices=config["versions"].keys(),
        type=str,
        help='Java version number'
    )
    parser.add_argument(
        '-g',
        '--global',
        dest="glob",
        action='store_true',
        help="Change java config on system, otherwise only the current terminal will be affected"
    )
    
    # Print help
    if len(sys.argv) == 1 or (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        parser.print_help(sys.stderr)
        log.warn("Be sure to have in PATH : %JAVA_BIN% ; %M2_BIN% and no other link to mvn & java")
        exit()   
    
    args = parser.parse_args()
    
    if not windows.existInPathUser("%JAVA_BIN%"):
        log.error("Ajouter %JAVA_BIN% dans le PATH")
        # print("setx PATH \"" + windows.getEnvVarUser('PATH') + ";%JAVA_BIN%;")
        exit()
    if not windows.existInPathUser("%M2_BIN%"):
        log.error("Ajouter %M2_BIN% dans le PATH")
        # print("setx PATH \"" + windows.getEnvVarUser('PATH') + ";%M2_BIN%;")
        exit()
    
    javaPath = config["versions"][args.version]["javaPath"]
    javaPathBin = config["versions"][args.version]["javaPath"] + "\\bin"
    mavenPath = config["versions"][args.version]["mavenPath"]
    mavenPathBin = config["versions"][args.version]["mavenPath"] + "\\bin"
    
    if args.glob:
        print("setx JAVA_BIN " + javaPathBin)
        print("setx JAVA_HOME " + javaPath)
        print("setx M2_BIN " + mavenPathBin)
        print("setx M2_HOME " + mavenPath)
    
    # Print commands to set environment variables
    print("set JAVA_BIN=" + javaPathBin)
    print("set JAVA_HOME=" + javaPath)
    print("set M2_BIN=" + mavenPathBin)
    print("set M2_HOME=" + mavenPath)
    
    refreshCmd = windows.getRegistrySystem(windows.systemRegDir, 'PATH') + ";" + windows.getRegistryUser(windows.defaultRegDir, 'PATH') + ";"
    print("CALL set \"PATH=" + refreshCmd + "\"")
    print("mvn -v")

if __name__ == '__main__':
    main()
