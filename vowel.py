def is_vowel(char):
    vowels = "aeiou"
    return char.lower() in vowels

# example usage
letter = "x"
if is_vowel(letter):
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
