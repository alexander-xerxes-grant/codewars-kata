

def spin_words(sentence):
    """
    Spin words in a sentence.
    """
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 4:
            words[i] = words[i][::-1]
    return ' '.join(words)