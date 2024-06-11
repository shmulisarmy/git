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


commit_sig = makeCommitSig(sentence_one, sentence_two)
    

print(f"{commit_sig = }")

