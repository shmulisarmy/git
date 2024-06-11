from valueTree import ValueTree
from database_interface import get_line, create_line, delete_line, get_all_lines





all_lines_tree = ValueTree()


# laod db into tree
all_lines = get_all_lines()
for line in all_lines:
    all_lines_tree.insertWithValue(line[1], line[0])









all_sentences_list = [None]








def makeCommitSig(fileName):
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


    return commit_sig


def applyCommitSig(commit_sig, fileName) -> list[str]:
    lines = [all_sentences_list[line] for line in commit_sig]    
    with open(fileName, 'w') as f:
        f.writelines(lines)
    return lines





def full_cycle(sentence: list[str]) -> list[str]:
    """test function"""
    commit_sig = makeCommitSig(sentence)
    print(f"{commit_sig = }")
    print(f"{applyCommitSig(commit_sig) = }")




print(f"{makeCommitSig('thoughts') = }")
