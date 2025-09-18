
#Reading the content of files
file1 = open('sample1.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()



#Error Handling
try:
    file1 = open('sample.txt','r')
    reading_file = file1.read()
    print(reading_file)
    file.close()
except FileNotFoundError:
    print('Error: The file \'sample.txt\' was not found')
