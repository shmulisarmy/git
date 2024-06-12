import os, sys, json
from utils import makeCommitSigFile, applyCommitSigFile, applyCommitSigFileFromId
from database_interface import create_fullCommit, get_fullCommit_by_name



def fullDirectoryCommit(commitMsg, fullDirName):
    """recursively walks through directory and creates commit sigs for all files"""
    fileCommitIds = []
    for root, dirs, files in os.walk(fullDirName):
        print(f"root: {root}")
        for file in files:
            id_of_file_commit = makeCommitSigFile(commitMsg, os.path.join(root, file))
            if id_of_file_commit != None:
                fileCommitIds.append(id_of_file_commit)
        for dir in dirs:
            fileCommitIds.extend(fullDirectoryCommit(commitMsg, os.path.join(root, dir)))


    return fileCommitIds

    
def applyDirectoryCommit(commitName, directoryName):
    _, directory, fileCommitIdsJson = get_fullCommit_by_name(commitName)
    assert directory == directoryName
    for fileCommitId in json.loads(fileCommitIdsJson):
        print(f"__debug__ fileCommitId: {fileCommitId}")
        applyCommitSigFileFromId(fileCommitId)


if len(sys.argv) < 4:
    print("usage: python3 fullCommit.py <commitName> <directory>")
    exit(1)


commitName = sys.argv[2]
directory = sys.argv[3]


if sys.argv[1] == "apply":
    applyDirectoryCommit(commitName, directory)
    exit(0)

if sys.argv[1] == "make":
    fileCommitIds = fullDirectoryCommit(commitName, directory)
    print(f"fileCommitIds: {fileCommitIds}")
    create_fullCommit(commitName, directory, json.dumps(fileCommitIds))
    exit(0)