# Write into a file. Creates the file if non existant
f = open('demo.txt', mode='w')
f.write('Hello from Python!\n')
f.close()

# Append data in the file
f = open('demo.txt', mode='a')
f.write('Hello again!\n')
f.write('-' * 30)
f.close()

# Reads the contents of the file
r = open('demo.txt', mode='r')
file_content = r.read()
print(file_content)
r.close()

# Getting file contents as a list
s = open('demo.txt', mode='r')
file_list = s.readlines()
print(file_list)
s.close()