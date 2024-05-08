import winreg
import log

defaultRegDir = 'Environment'
systemRegDir = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

def insertInPathUser(value):
    if not existInPathUser(value):
        path = getEnvVarUser('PATH')
        index = path.find(';')
        newPathValue = path[:index] + ';' + value + path[index:]
        setEnvVarUser('PATH', newPathValue)
    
def insertInPathSystem(value):
    if not existInPathSystem(value):
        path = getEnvVarSystem('PATH')
        index = path.find(';')
        newPathValue = path[:index] + ';' + value + path[index:]
        setEnvVarSystem('PATH', newPathValue)
        
def existInPathUser(value):
    pathValue = getEnvVarUser('PATH')
    return value + ";" in pathValue

def existInPathSystem(value):
    pathValue = getEnvVarSystem('PATH')
    return value + ";" in pathValue

def setEnvVarUser(key, value):
    setRegistryUser(defaultRegDir, key, value)
    
def getEnvVarUser(key):
    return getRegistryUser(defaultRegDir, key)

def setEnvVarSystem(key, value):
    setRegistrySystem(systemRegDir, key, value)
    
def getEnvVarSystem(key):
    return getRegistrySystem(systemRegDir, key)

def getRegistryUser(regdir, keyname):
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, regdir) as accessRegistryDir:
        value, _ = winreg.QueryValueEx(accessRegistryDir, keyname)
        return(value)
    
def setRegistryUser(regdir, keyname, keyvalue):
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, regdir) as _:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, regdir, 0, winreg.KEY_WRITE) as writeRegistryDir:
            winreg.SetValueEx(writeRegistryDir, keyname, 0, winreg.REG_SZ, keyvalue)
            
def getRegistrySystem(regdir, keyname):
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regdir) as accessRegistryDir:
        value, _ = winreg.QueryValueEx(accessRegistryDir, keyname)
        return(value)
    
def setRegistrySystem(regdir, keyname, keyvalue):
    try:
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, regdir) as _:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regdir, 0, winreg.KEY_WRITE) as writeRegistryDir:
                winreg.SetValueEx(writeRegistryDir, keyname, 0, winreg.REG_SZ, keyvalue)
    except PermissionError:
        log.error("Use admin terminal")
        exit()