import os
import conf

config = conf.load('weblo-conf.json')

def main():
    os.system(config['path'])

if __name__ == "__main__":
    main()
