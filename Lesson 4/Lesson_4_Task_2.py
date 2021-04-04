# Lesson 4 Task 2

#input_string = input('Enter the string: ')

input_string = 'jefv kowek pmefpqd iutjwdcv jekv a b c d prge'
search_char = input('Enter the symbol you want to search: ')

while len(search_char) > 1:
        search_char = input('Please, enter only one symbol: ')
found_counter = 0
search_index = 0

if input_string.find(search_char) == -1:
        print('Sorry, we did not found symbol in input string.')
else:
        print(f'Symbol \'{search_char}\' is on positions: ', end='')

        while search_index < len(input_string):
                find_index = input_string.find(search_char, search_index)
                if find_index == -1:
                        break
                print(f'{find_index}, ', end='')
                found_counter += 1
                search_index = find_index + 1
        print('\b\b.')
        print(f'Input string has {found_counter} searched symbols.')