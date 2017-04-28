file = open("exampleWrite.txt", "w")
file.write("Line 2")
file.close()

file2 = open("exampleWrite2.txt", 'w')
l = ['line1', 'line2', 'line3']

for item in l:
    file2.write(item + '\n')

file2.close()