import random

color = ['S', 'H', 'D', 'C']
points = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

card_list = []
for c in color:
    for p in points:
        card_list.append(c + p)

print(card_list)

random.shuffle(card_list)

print(card_list)

player1 =  []
player2 =  []
player3 =  []
player4 =  []

i = 1

for c in card_list:
    if i % 4 == 1:
        player1.append(c)
    elif i % 4 == 2:
        player2.append(c)
    elif i % 4 == 3:
        player3.append(c)
    else:
        player4.append(c)
    i += 1
    

print(player1)
print(player2)
print(player3)
print(player4)

print(random.choice(player1)) 
print(random.choice(player2)) 
print(random.choice(player3)) 
print(random.choice(player4)) 