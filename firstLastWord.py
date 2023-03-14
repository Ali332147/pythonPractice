sentence = "Hello, World! This is a sample sentence."

words = sentence.split()

if len(words) >= 1:
    print("First word:", words[0])
    print("Last word:", words[-1])
else:
    print("The input sentence is empty.")
