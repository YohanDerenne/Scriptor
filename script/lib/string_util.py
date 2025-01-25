import json

def dictionnaryToString(dictionnary) -> str :
    return json.dumps(dictionnary).replace(",", ",\n").replace("{", "").replace("}", "")