# no need to close file using "with" statement

with open('example.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    file.write('\nline 11')