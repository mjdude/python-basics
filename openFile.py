file = open("example.txt", 'r');

content = file.read();
print(content)

# navigate back to begging of text file
file.seek(0)
content=file.readlines();

print(content)