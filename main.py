import os, json, sys
from valueTree import ValueTree
from database_interface import get_line, create_line, delete_line, get_all_lines, get_lines_in, get_fileCommit, create_fileCommit, delete_fileCommit, get_all_fileCommits, getCommitByName





all_lines_tree = ValueTree()


# laod db into tree
all_lines = get_all_lines()
for line in all_lines:
    all_lines_tree.insertWithValue(line[1], line[0])



def makeCommitSigFile(commitName, fileName):
    with open(fileName) as f:
        lines = f.readlines()
    commit_sig = []
    for word in lines:
        value = all_lines_tree.getValue(word)
        if value == None:
            #create a value for it while placing it in the tree
            value = create_line(word)
            all_lines_tree.insertWithValue(word, value)

        commit_sig.append(value)


    create_fileCommit(commitName, json.dumps(commit_sig), os.path.basename(fileName))



    return commit_sig


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



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python main.py makeCommitSigFile <commitName> <fileName>")
        print("or: python main.py applyCommitSigFile <commitName> <fileName>")
        exit(1)
    if sys.argv[1] == "makeCommitSigFile":
        makeCommitSigFile(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "applyCommitSigFile":
        applyCommitSigFile(sys.argv[2], sys.argv[3])


