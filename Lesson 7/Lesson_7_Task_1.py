# Lesson 7 Task 1

print('Our new list is: ', list(map(lambda item:
               (item[0], (round(item[2] * item[3] ,2)
                          if round(item[2] * item[3] ,2) > 100
                          else round(item[2] * item[3] ,2) + 10)),
                                    [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
                                    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
                                    [77226, 'Head First Python, Paul Barry', 3, 32.95],
                                    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]])))






