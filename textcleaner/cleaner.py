import string

def clean_sentence(sentence):
    translator = str.maketrans("", "", string.punctuation)
    cleaned = sentence.translate(translator)
    words = cleaned.lower().split()
    return sorted(set(words))
