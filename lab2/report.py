import json


filename = raw_input('Type the file name > ' ) #using the raw_input to open 'data/test.json'
infile = open(filename)
student = json.load(infile)
infile.close() #close infile

name = student['name']
grades = student['grades']

#print the grade info 
print "."*70
print name, 'got a ',grades['lab1']['earned'],' out of ',grades['lab1']['possible'],' on lab1'
print name, 'got a ',grades['lab2']['earned'],' out of ',grades['lab2']['possible'],' on lab2'
print name, 'got a ',grades['lab3']['earned'],' out of ',grades['lab3']['possible'],' on lab3'
print "."*70
