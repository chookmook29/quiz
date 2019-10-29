import random
import csv
import re

with open('trmtrkt.csv', mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	row = [r for r in csv_reader]
	random = random.randint(2, 501)
	attr_list = row[random]
	position = str(attr_list[2])
	cropped = attr_list[0]
	cropped = re.findall('([A-Z])', cropped)
	one_string = ''
	for letter in cropped:
		one_string = one_string + letter + '. '
	check = 'midfield' in position
	if check:
		position = position + 'er'
	print(f'{attr_list[5]} years old {position} from {attr_list[1]} worth {attr_list[3]}.\nRepresents {attr_list[4]}.\nSo far played in {attr_list[6]} league games this season.')
	print(f'Initials are: {one_string}')
	decision = input(f'Check?')
	print(attr_list[0])
