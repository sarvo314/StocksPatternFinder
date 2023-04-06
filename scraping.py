#reg expression
import re

# Open the input file for reading
with open('scraping.txt', 'r') as file:

	# Read the contents of the file
	content = file.read()
	matches = set()
	# Find all uppercase words that end with .NS using regular expressions
	all_matches = re.findall(r'\b[A-Z]+\.NS\b', content)
	for item in all_matches:
		matches.add(item)		
	print(matches)

with open('output.txt', 'w') as file:
	for match in matches:
		file.write(match + '\n')
