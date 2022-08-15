def spin_words(sentence):
    sesentence_list = sentence.split(' ')
    for index, elem in enumerate(sesentence_list):
        if len(elem) >= 5:
            sesentence_list[index] = ''.join(reversed(elem))
    new_sentence = ' '.join(sesentence_list)
    return new_sentence


a = spin_words('Hey fellow warriors')
print(a)
