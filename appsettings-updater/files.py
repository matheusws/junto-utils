import os, shutil, csv, constants

def createAppFoldersAndFiles():
    folders = [constants.BACKUP_FOLDER,
               constants.TMP_FOLDER,
               constants.INPUT_FOLDER]
    files = [constants.PROJECTS_FILE,
             constants.REPLACEMENTS_FILE]

    for folder in folders:
        folderPath = os.path.join(constants.CURRENT_PATH, folder)
        if not os.path.exists(folderPath):
            os.mkdir(folderPath)
    
    for file in files:
        filePath = os.path.join(constants.CURRENT_PATH, constants.INPUT_FOLDER, file)
        if not os.path.exists(filePath):
            newFile = open(filePath, "w")
            if file == constants.REPLACEMENTS_FILE:
                newFile.write("original,replacement\n")
            newFile.close()

def readFileContent(filePath):
    file = open(filePath, "r")
    fileContent = file.read()
    file.close()

    return fileContent

def readProjects():
    projectsPath = os.path.join(constants.CURRENT_PATH, constants.INPUT_FOLDER, constants.PROJECTS_FILE)
    projects = readFileContent(projectsPath)

    if len(projects) > 0:
        return projects.split("\n")
    
    return []

def readReplacements():
    replacementsPath = os.path.join(constants.CURRENT_PATH, constants.INPUT_FOLDER, constants.REPLACEMENTS_FILE)
    fileContent = []

    with open(replacementsPath, newline='\n') as replacementsFile:
        reader = csv.DictReader(replacementsFile)
        for row in reader:
            line = {"original": row["original"], "replacement": row["replacement"]}
            fileContent.append(line)

    return fileContent

def copyFile(filePath, destination):
    shutil.copyfile(filePath, destination)

def deleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

def matchReplacement(line, replacements):
    for replacement in replacements:
        if line.rfind(replacement["original"]) > -1:
            return replacement
    return None

def replaceLine(line, replacement):
    return line.replace(replacement["original"], replacement["replacement"])