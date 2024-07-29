# Get sentence from user
original = input("Please enter a sentence: ").strip().lower()

# Split the sentence into words
words = original.split()

# Loop through words and convert to Pig Latin
new_words = []

for word in words:
    # If word starts with vowels just add 'yay'
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        # Otherwise, move the first consonant cluster to end, and add 'ay'
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        new_word = rest + cons + "ay"
        new_words.append(new_word)

# Stick words back together
output = " ".join(new_words)

# Output the string
print(output)
