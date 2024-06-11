from custom_packages.searchTree import SearchTree





sentence_one = ["hello", "shmuli", "hey", "bye"]
sentence_two = ["hello", "hey", "shmuli", "bye"]










def makeCommitSig(sentence_one, sentence_two):
    sentence_one_all_tree = SearchTree()
    for i in range(len(sentence_one)):
        word = sentence_one[i]
        sentence_one_all_tree.insertWithValue(word, i)

    commit_sig = []
    for word in sentence_two:
        print(f"{word = }")
        value =  sentence_one_all_tree.getValue(word)
        print(f"{sentence_one_all_tree.getValue(word) = }")
        if value != None:
            commit_sig.append(value)
        else:
            commit_sig.append(word)


    return commit_sig


def applyCommitSig(sentence_to_create_from, commit_sig):
    outcome_sentence = []
    for word_or_line in commit_sig:
        if type(word_or_line) == int:
            outcome_sentence.append(sentence_to_create_from[word_or_line])
        else:
            # word_or_line == word
            outcome_sentence.append(word_or_line)
    return outcome_sentence



commit_sig = makeCommitSig(sentence_one, sentence_two)
    

print(f"{commit_sig = }")
print(f"{applyCommitSig(sentence_one, commit_sig) = }")

