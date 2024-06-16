#Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

str1 = "The lyrics is poor!"
text_to_remove = "poor"
text_to_add = "good"
result = str1.replace(text_to_remove, text_to_add)
print(result)
