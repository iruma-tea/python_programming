import string


with open('design/email_template.txt') as file:
    t = string.Template(file.read())
    contents = t.substitute(name='Mike', contents='How are you?')
    print(contents)
