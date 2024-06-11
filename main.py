from custom_packages.searchTree import SearchTree








sentence_one = ["hello", "shmuli", "hey", "bye"]
sentence_two = ["hello", "hey", "shmuli", "bye"]
sentence_three = ["hey", "shmuli", "bye", "djalskdj", "hello"]


all_sentences_list = [None]

all_sentences_tree = SearchTree()
all_sentences_tree.word_count = 0







def makeCommitSig(sentence_sig_is_for):
    commit_sig = []
    for word in sentence_sig_is_for:
        value = all_sentences_tree.getValue(word)
        if value == None:
            all_sentences_list.append(word)
            all_sentences_tree.word_count += 1
            value = all_sentences_tree.word_count
            #create a value for it while placing it in the tree
            all_sentences_tree.insertWithValue(word, value)

        commit_sig.append(value)


    return commit_sig


def applyCommitSig(commit_sig) -> list[str]:
    return [all_sentences_list[line] for line in commit_sig]    





def full_cycle(sentence: list[str]) -> list[str]:
    commit_sig = makeCommitSig(sentence)
    print(f"{commit_sig = }")
    print(f"{applyCommitSig(commit_sig) = }")


full_cycle(sentence_one)
full_cycle(sentence_two)
full_cycle(sentence_three)

