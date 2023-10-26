import os, re, platform

def isLinux():
    currentOs = platform.system()
    return currentOs.lower() == "linux"

def convertWindowsToUnixPath(windowsPath):
    regex = re.compile("[a-zA-Z]\:{1}")
    match = regex.search(windowsPath)

    if not match:
        raise Exception(f"Caminho inválido: {windowsPath}")
    
    replacedPath = windowsPath.replace("\\", "/")
    replacedPath = replacedPath.replace(match[0], f"mnt/{match[0].replace(':', '').lower()}")

    return f"/{replacedPath}"

def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

def getFileNameFromPath(projectPath):
    spplitedPath = os.path.split(projectPath)
    return spplitedPath[len(spplitedPath) - 1]
