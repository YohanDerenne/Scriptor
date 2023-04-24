import json
import os
import log

confFolder = os.path.dirname(__file__) + '/../config/'

def load(jsonFileName):
    configPath = confFolder + jsonFileName

    try:
        with open(configPath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        log.error('Le fichier de configuration \"' + jsonFileName + 
                  "\" est introuvable dans le dossier " + os.path.realpath(confFolder))
        exit()