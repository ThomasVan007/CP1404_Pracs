sting = input("Please enter a sentence:")
unique_words = {}
words = sting.split()
for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1
words = list(unique_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))