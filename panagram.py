import string

def is_pangram(sentence):
    # convert sentence to lowercase and remove non-alphabetic characters
    sentence = sentence.lower()
    sentence = ''.join(filter(str.isalpha, sentence))

    # create a set of all the letters in the alphabet
    alphabet = set(string.ascii_lowercase)

    # check if the set of letters in the sentence is equal to the alphabet set
    return set(sentence) == alphabet

# example usage
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print(f"{sentence} is a pangram")
else:
    print(f"{sentence} is not a pangram")
