def single_root_words(root_word, *other_word):
    root_word = root_word.lower()
    same_words = []
    
    for word in other_word:
        l_word = word.lower()
        if l_word in root_word or root_word in l_word:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)