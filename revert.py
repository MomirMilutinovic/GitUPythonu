import os
import shutil
from add import copy 

def getBackupFile(repositoryPath):
    #Vraca backups file
    return repositoryPath + '\\.backups'
    
def revertToCommit(repository, commit):
    #Kao parametar prima pud do repozitorijuma i sting u kom je broj komita na koji se vraca
    #Vraca repozitorijum u stanje nekog prošlog komita
    
    backupPath = getBackupFile(repository)
    
    #Brise working directory
    for the_file in os.listdir(repository):
        file_path = os.path.join(repository, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path) and (not(file_path == repository+'\\.backups')): 
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)
           
    file_path = os.path.join(backupPath, commit)
    print(file_path)
    for the_file in os.listdir(file_path):
        copy_path = os.path.join(file_path, the_file)
        copy(copy_path, repository + '\\' + the_file) 
    