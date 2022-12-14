from classes import Game
import requests
import random

headers = {'Accept': 'application/json'}

r = requests.get('https://rps101.pythonanywhere.com/api/v1/objects/all', headers=headers)

all_objects = list(r.json())
b = []
w = []
for i in all_objects:
    r = requests.get('https://rps101.pythonanywhere.com/api/v1/objects/' + i, headers=headers)
    winning_outcomes = [x[1] for x in list(dict(r.json())["winning outcomes"])]
    b.extend([i for j in winning_outcomes])
    w.extend(winning_outcomes)

g = Game(all_objects,b,w,generateImages=False)

names = g.getNames()
while True:
    element_input = input("Enter Choice: ")
    try:
        element_input = element_input[0].upper() + element_input[1:].lower()
    except Exception as e:
        print("Please input a value.")
        continue
    element_random = random.choice(names)
    if element_input == "Exit":
        break
    try:
        winner = g.whoWins(element_input,element_random)
        print("You chose: " + str(element_input) + " and Computer chose: " + str(element_random))
        print("Winner: " + str(winner))
    except Exception as e:
        print("Bad input. Try again.")