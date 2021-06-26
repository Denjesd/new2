# Lesson 4 Task 4

input_string = 'ejefv kowek pmefpqd iutjwdcv jekv a b ce d prge'
upper_char = input('Enter the symbol you want to capitalize (except the first and the last): ')
while len(upper_char) > 1:
    upper_char = input('Please, enter only one symbol: ')
print(f'Input string is: \'{input_string}\'.')

first_meeting = input_string.find(upper_char)

if first_meeting == -1:
    print('Sorry, we did not found symbol in input string.')
else:

    last_meeting = input_string.rfind(upper_char)

    first_part = input_string[:first_meeting + 1]
    last_part = input_string[last_meeting:]
    central_part = input_string[first_meeting + 1:last_meeting]

    result_string = first_part + central_part.replace(upper_char, upper_char.upper()) + last_part
    print(f'Result string is: \'{result_string}\'.')