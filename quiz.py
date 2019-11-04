import random
import csv
import re


round_number = 1
player_1 = 0
player_2 = 0
name_1 = input('Player 1 name?')
name_2 = input('Player 2 name?')

while round_number < 6:
	print('*******************')
	print(f'Question for you {name_1}')
	with open('trmtrkt.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = [r for r in csv_reader]
		random_roll = random.randint(2, 501)
		attr_list = row[random_roll]
		position = str(attr_list[2])
		cropped = attr_list[0]
		cropped = re.findall('([A-Z])', cropped)
		points = int(attr_list[7])
		negative_points = int(attr_list[7]) - 21
		one_string = ''
		for letter in cropped:
			one_string = one_string + letter + '. '
		check = 'midfield' in position
		if check:
			position = position + 'er'
		print(f'{attr_list[5]} years old {position} from {attr_list[1]} worth {attr_list[3]}.\nRepresents {attr_list[4]}.\nSo far played in {attr_list[6]} league games this season.')
		print(f'Initials are: {one_string}')
		print(f'{points} point(s) if correct, {negative_points} point(s) if wrong.')
		decision = input(f'Check?')
		print(attr_list[0])
		result = input(f'Guessed?')
		if result == 'y':
			player_1 += points
		else:
			player_1 += negative_points
	print('*******************')
	print(f'Question for you {name_2}')
	with open('trmtrkt.csv', mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = [r for r in csv_reader]
		random_roll = random.randint(2, 501)
		attr_list = row[random_roll]
		position = str(attr_list[2])
		cropped = attr_list[0]
		cropped = re.findall('([A-Z])', cropped)
		points = int(attr_list[7])
		negative_points = int(attr_list[7]) - 21
		one_string = ''
		for letter in cropped:
			one_string = one_string + letter + '. '
		check = 'midfield' in position
		if check:
			position = position + 'er'
		print(f'{attr_list[5]} years old {position} from {attr_list[1]} worth {attr_list[3]}.\nRepresents {attr_list[4]}.\nSo far played in {attr_list[6]} league games this season.')
		print(f'Initials are: {one_string}')
		print(f'{points} point(s) if correct, {negative_points} point(s) if wrong.')
		decision = input(f'Check?')
		print(attr_list[0])
		result = input(f'Guessed?')
		if result == 'y':
			player_2 += points
		else:
			player_2 += negative_points
	print('*******************')
	print(f'{round_number} Round summary:')
	print(f'{name_1} points: {player_1}')
	print(f'{name_2} points: {player_2}')
	round_number += 1
print('*******************')
print(f'FINAL RESULT:')
print(f'{name_1} points: {player_1}')
print(f'{name_2} points: {player_2}')
