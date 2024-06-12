import os, json, sys
from valueTree import ValueTree
from database_interface import get_line, create_line, get_all_lines, get_lines_in, get_fileCommit, create_fileCommit, get_all_fileCommits, getCommitByName




all_lines_tree = ValueTree()


# laod db into tree
all_lines = get_all_lines()
for line in all_lines:
    all_lines_tree.insertWithValue(line[1], line[0])


def makeCommitSigFile(commitName, fileName):
    if not os.path.exists(fileName):
        print(f"file not found: {fileName}")
        exit(1)
    # check if file is able to be read
    try:
        with open(fileName) as f:
            lines = f.readlines()
            print(f"reading file: {fileName}")
    except:
        print(f"file ends in .db: {fileName}")
        return None

    commit_sig = []
    for word in lines:
        value = all_lines_tree.getValue(word)
        if value == None:
            #create a value for it while placing it in the tree
            value = create_line(word)
            all_lines_tree.insertWithValue(word, value)

        commit_sig.append(value)


    return create_fileCommit(commitName, json.dumps(commit_sig), fileName)


def applyCommitSigFileFromId(fileCommitId):
    _, commitSigJson, fileName = get_fileCommit(fileCommitId)
    print(f"writing to file: {fileName}")
    with open(fileName, 'w') as f:
        for line_id in json.loads(commitSigJson):
            line = get_line(line_id)
            print(f"__debug__ line: {line} in file: {fileName}")
            f.write(line[0])
        


def applyCommitSigFile(commitName, fileName) -> list[str]:
    fileCommit = getCommitByName(commitName)
    print(f"__debug__ fileCommit: {fileCommit}")
    commitSigJson = fileCommit[2]
    print(f"__debug__ commitSigJson: {commitSigJson}")
    commitSig = json.loads(commitSigJson)
    print(f"__debug__ commit_sig_for_file: {commitSig}")
    lines = [i[1] for i in get_lines_in(commitSig)]
    with open(fileName, 'w') as f:
        f.writelines(lines)
    return lines
