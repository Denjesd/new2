# Lesson 7 Task 1
input_list = [
                [34587, 'Learning Python, Mark Lutz', 4, 10.95],
                [98762, 'Programming Python, Mark Lutz', 5, 56.80],
                [77226, 'Head First Python, Paul Barry', 3, 32.95],
                [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99],
             ]

print('Our new list is:', list(map(lambda item: (
                                    item[0],
                                    round(item[2] * item[3]
                                        if item[2] * item[3] >= 100
                                        else
                                            item[2] * item[3] + 10, 2)
                                                ),
                                    input_list
                                    )
                                )
      )








