import re, os, utils, files, myLogging, constants

#todo: validar se input existe
#todo: validar formato do arquivo csv
#todo: replace para projetos em C#
#todo: replace para projetos em node
#todo: deletar backup?

files.createAppFoldersAndFiles()

projects = files.readProjects()
replacements = files.readReplacements()

if len(projects) <= 0 or len(replacements) <=0:
    myLogging.logError("Um dos arquivos de entrada esta vazio")

for project in projects:
    projectPath = utils.convertWindowsToUnixPath(project) if utils.isLinux() else project
    appsettings = []

    regex = re.compile("appsettings\.[a-zA-Z0-9]{1,}\.json")

    for root, dirs, dirFiles in os.walk(projectPath):
        matches = [os.path.join(root, f) for f in dirFiles if regex.match(f)]
        if len(matches) > 0: appsettings.extend(matches)

    appsettingsBackupPath = os.path.join(constants.CURRENT_PATH, constants.BACKUP_FOLDER, utils.getFileNameFromPath(projectPath))
    utils.createFolder(appsettingsBackupPath)

    for appsetting in appsettings:
        projectName = utils.getFileNameFromPath(appsetting)
        tmpFile = os.path.join(constants.CURRENT_PATH, constants.TMP_FOLDER, f"{projectName}_tmp.json")
        
        files.copyFile(appsetting, os.path.join(appsettingsBackupPath, projectName))

        try:
            with open(appsetting, "r") as appsettingFile:
                with open(tmpFile, "w") as outputFile:
                    while True:
                        line = appsettingFile.readline()
                        if not line:
                            break

                        matchingReplacement = files.matchReplacement(line, replacements)
                        
                        if matchingReplacement:
                            replacedLine = files.replaceLine(line, matchingReplacement)
                            outputFile.write(replacedLine)
                        else:
                            outputFile.write(line)

            files.copyFile(tmpFile, appsetting) 
        except:
            myLogging.logError(f"Erro ao ler arquivo: {appsetting}")
        finally:
            outputFile.close()
            appsettingFile.close()
            files.deleteFile(tmpFile)
        
exit()