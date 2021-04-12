# Lesson 6 Task 1

except_symbols = ('.', ',', '!', '?', ';', ':', '\'', '(', ')', '\"')
input_words = open('Lesson_6_1.txt').read().lower().split()
dict_words = {}
max_word_appearence = ['', 1]

for word in range(len(input_words)):
    listed_word = list(input_words[word])

    index = 0
    while index < len(listed_word):
        if listed_word[index] in except_symbols:
            listed_word.pop(index)
        else:
            index += 1

    word_to_dict = ''.join([elem for elem in listed_word])
    if dict_words.get(word_to_dict) is None:

        dict_words[word_to_dict] = 1
    else:
        dict_words[word_to_dict] += 1
        if dict_words.get(word_to_dict) >= max_word_appearence[1]:
            max_word_appearence[0] = word_to_dict
            max_word_appearence[1] = dict_words.get(word_to_dict)

for word in dict_words:
    print(word, dict_words.get(word))
print(f'The most frequent word is \'{max_word_appearence[0]}\''
      f' with {max_word_appearence[1]} times appearence.')
