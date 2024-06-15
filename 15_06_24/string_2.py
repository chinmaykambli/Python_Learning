def len_of_fun(str1):
    if len(str1) < 2:
        return ''

    return str1[0: 2] + str1[-4: ]

print(len_of_fun('My_name_is_khan'))

