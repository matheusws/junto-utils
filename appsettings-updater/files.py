import os, shutil, csv, constants

def readFileContent(filePath):
    file = open(filePath, "r")
    fileContent = file.read()
    file.close()

    return fileContent

def readProjects():
    projectsPath = os.path.join(constants.CURRENT_PATH, constants.INPUT_FOLDER, constants.PROJECTS_FILE)
    return readFileContent(projectsPath).split("\n")

def readReplacements():
    replacementsPath = os.path.join(constants.CURRENT_PATH, constants.INPUT_FOLDER, constants.REPLACEMENT_FILE)
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