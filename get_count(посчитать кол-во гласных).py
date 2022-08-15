def get_count(sentence):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    for elem in sentence.lower():
        if elem in vowels_list:
            vowels_count += 1
    return vowels_count


a = get_count('12E123Ou')
print(a)
