#program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String
def len_of_fun(str1):
    if len(str1) < 2:
        return ''

    return str1[0: 2] + str1[-4: ]

print(len_of_fun('My_name_is_khan'))

