def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letters in sentence:
        if letters in vowels:
            count += 1
    return count if count > 0 else 0