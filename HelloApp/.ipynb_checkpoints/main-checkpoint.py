# Online Python—IDE, Editor, Compiler, Interpreter

#       ДЗ № 3+
# Списки и словари в Python

sentence = input("Enter a sentence: ")

word_count = {}
for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

num_unique_words = len(word_count)

most_frequent_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        most_frequent_word = word
        max_count = count

print("The sentence contains", num_unique_words, "unique words.")
print("The most frequent word is:", most_frequent_word)
