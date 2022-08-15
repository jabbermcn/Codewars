def anagrams(word, words):
    new_list = []
    for elem in words:
        if sorted(word) == sorted(elem):
            new_list.append(elem)
    return new_list


a = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(a)
