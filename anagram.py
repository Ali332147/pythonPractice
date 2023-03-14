def is_anagram(s1, s2):
    # convert strings to lowercase and remove whitespace
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')

    # check if the sorted strings are equal
    return sorted(s1) == sorted(s2)

# example usage
word1 = "race"
word2 = "care"
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")
