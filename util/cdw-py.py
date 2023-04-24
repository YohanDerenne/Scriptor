import os
import sys
import subprocess
import glob

def main():
    # CONF
    pathWS18 = r"C:\usine-dev\workdir\workspace18"
    pathWS17 = r"C:\usine-dev\workdir\workspace17"
    pathWS16 = r"C:\usine-dev\workdir\workspace16"
    pathWS = r"C:\usine-dev\workdir\workspace"
    versionJava6 = "1.6.0_45"
    versionJava7 = "1.7.0_79"
    versionJava8 = "1.8.0_191"

    # Root sans args
    if len(sys.argv) == 1:
        version = subprocess.run(
            ['java', '-version'], capture_output=True, text=True).stderr
        # print("version : " + version)
        if versionJava6 in version:
            path = pathWS16
        if versionJava7 in version:
            path = pathWS17
        if versionJava8 in version:
            path = pathWS18
        print(path)
        exit(0)

    # VAR
    # print(os.getcwd())
    # os.chdir("C:/usine-dev/workdir/workspace18/SAE")
    # subprocess.run('cd C:/usine-dev/', shell=True)
    project = "\\" + sys.argv[1]

    path = pathWS18 + project
    findProjectAndStopIfExist(path, sys.argv[2:])

    path = pathWS17 + project
    findProjectAndStopIfExist(path, sys.argv[2:])

    path = pathWS16 + project
    findProjectAndStopIfExist(path, sys.argv[2:])
    
    path = pathWS + project
    findProjectAndStopIfExist(path, sys.argv[2:])
    
    findProjectAndStopIfExist(".", sys.argv[1:])

    print('Projet introuvable')
    exit(1)


def findProjectAndStopIfExist(path, sousProjets):
    if os.path.isdir(path):
        cdPath = path
        for sp in sousProjets:
            dirs = glob.glob(cdPath + "\\*" + sp)
            if len(dirs) == 1 and os.path.isdir(dirs[0]):
                cdPath = dirs[0]
            else:
                break
        if len(cdPath) > 1 :  
            print(cdPath)
            exit(0)


if __name__ == '__main__':
    main()
