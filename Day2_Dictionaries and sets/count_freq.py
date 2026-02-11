from collections import Counter

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

word_count = Counter(words)

print("\nWord Frequency:", word_count)
