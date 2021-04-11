# Lesson 6 Task 1

exept_symbols = ('.', ',', '!', '?', ';', ':', '\'', '(', ')', '\"')
input_words = open('Lesson_6_1.txt').read().lower().split()
dict_words = {}

for word in range(len(input_words)):
    listed_word = list(input_words[word])

    index = 0
    while index < len(listed_word):
        if listed_word[index] in exept_symbols:
            listed_word.pop(index)
        else:
            index += 1

    word_to_dict = ''.join([elem for elem in listed_word])
    if dict_words.get(word_to_dict) == None:

        dict_words[word_to_dict] = 1
    else:
        dict_words[word_to_dict] += 1

for word in dict_words:
    print(word, dict_words.get(word))
