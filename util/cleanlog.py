import argparse
import os
import re
import conf
import log

# Load Config
config = conf.load('cleanlog-conf.json')

def main():    
    # Arg manager
    parser = argparse.ArgumentParser(description="Clean history log files", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'path',
        choices=config.keys(),
        type=str,
        help='Key path to log directory'
    )
    
    # Parse Args
    args = parser.parse_args()
    
    # Regex old log files
    PATTERN_DATE = "[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])"
    PATTERN_EXT_LOG = "\\.log"
    regex = re.compile('.*(' + PATTERN_DATE + '.*' + PATTERN_EXT_LOG + '|' + PATTERN_EXT_LOG + '.*' + PATTERN_DATE + ".*)")

    # Get list of old log files path
    logDir = config[args.path]
    log.info("Searching log files to delete in " + logDir + "...")
    filesToDelete = []
    for root, dirs, files in os.walk(logDir):
        for file in files:
            if regex.match(file):
                path = root + os.sep + file
                print(r"" + path)
                filesToDelete.append(path)
                
    if len(filesToDelete) == 0:
        log.info("No files to delete")
        exit()
    
    if input(str(len(filesToDelete)) + " files to delete found. Are you sure to process delete? (y/n)") != "y":
        log.error("Operation canceled")
        exit()

    for file in filesToDelete:
        os.remove(file)
    
    log.sucess(str(len(filesToDelete)) + " files has been cleaned")

if __name__ == '__main__':
    main()
