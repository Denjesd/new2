# Lesson 6 Task 3

d = {
    'apple': ['malum', 'pomum', 'popula', 'hfbb'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa'],
    'ares': ['hfbb', 'poppa', 'popum'],
    'pluto': ['popula', 'multa', 'hfbb']
}
d2 = {}


for word in d:
    for value in d.get(word):
        if d2.get(value) is None:
          d2[value] = [word]
        else:

          d2[value].append(word)
          pass
for key, value in d2.items():
    print(key, ':', value)
