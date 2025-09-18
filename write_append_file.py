
#Write the content to file
file1 = open('output.txt','w')
writing_file = file1.write('Hello, Python!')
print(writing_file)
file1.close()

#Append the content to file
file1 = open('output.txt','a')
append_file = file1.write('\nLearning file handling in Python.')
print(append_file)
file1.close()

#Read the content of file
file1 = open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
