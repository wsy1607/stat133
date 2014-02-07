# First import the Python JSON package
import json

student = {"name": "Student A",
			"grades": {
			"lab1": {
				"earned": 9,
				"possible": 12},
			"lab2": {
				"earned": 12,
				"possible": 15},
			"lab3": {
				"earned": 20,
				"possible": 22},
		},
}

### begin CORRECTION NEEDED
from sys import argv  #using argv for input 'data/test.json'

script, filename = argv
outfile = open(filename, 'w') 
json.dump(student, outfile, sort_keys = True, indent = 4)
outfile.close()
### end CORRECTION NEEDED