string = "I Love Flower"

# Use string manipulation and a loop to count the total number of letters in the string
count = 0
for char in string:
    if char.isalpha():
        count += 1

print("{}  contains {} Letters.".format(string, count))
# Output: The string 'I Love Flower' contains 11 letters.
