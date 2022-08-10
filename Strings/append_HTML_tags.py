''' 15. Write a Python function to create the HTML string with tags around the word(s). Go to the editor
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' '''
tags = input('Enter the tags which you want to append ')
content = input('Enter the content which you want to append the tag with ')
result = '<' + tags + '>' + content + '<' + tags + '>'
print(result)