import argparse
import os
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
        choices=config.keys(),
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
    
    javaPath = config[args.version]["javaPath"]
    javaPathBin = config[args.version]["javaPath"] + "\\bin"
    mavenPath = config[args.version]["mavenPath"]
    mavenPathBin = config[args.version]["mavenPath"] + "\\bin"
    
    if args.glob:
        log.warn("Admin rights required")

        # Check requirement
        if not windows.existInPathSystem("%JAVA_BIN%"):
            log.error("Ajouter %JAVA_BIN% dans le PATH Systeme (admin)")
            # print("setx PATH \"" + windows.getEnvVarUser('PATH') + ";%JAVA_BIN%;")
            exit()
        if not windows.existInPathSystem("%M2_BIN%"):
            log.error("Ajouter %M2_BIN% dans le PATH Systeme (admin)")
            # print("setx PATH \"" + windows.getEnvVarUser('PATH') + ";%M2_BIN%;")
            exit()
        
        # Apply
        print("setx JAVA_BIN " + javaPathBin)
        print("setx JAVA_HOME " + javaPath)
        print("setx M2_BIN " + mavenPathBin)
        print("setx M2_HOME " + mavenPath)
    
    # Print commands to set environment variables
    print("set JAVA_BIN=" + javaPathBin)
    print("set JAVA_HOME=" + javaPath)
    print("set M2_BIN=" + mavenPathBin)
    print("set M2_HOME=" + mavenPath)
    
    refreshCmd = os.environ['PATH']
    print("CALL set \"PATH=" + javaPathBin + ";" + mavenPathBin + ";" + refreshCmd + "\"")
    print("mvn -v")

if __name__ == '__main__':
    main()
