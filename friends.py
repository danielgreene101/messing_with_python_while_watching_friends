import random
import sys
import os

print("hello world")

friend = ["Rachael", "Ross", "Chandler", "Phoebe", "Joey", "Monica"]
print friend

print('Best of the friends = ', friend[2])

friend[2] = "Ross"

print('The worst of the friends is', friend[2])

friend[2] = "Chandler"

print("The funny friends are", friend[2:5])

print(random.choice(friend))

print(random.choice(friend), "is at the door")

print(friend)

my_friends = ["Noah", "Bobby", "Emily", "Marcella"]

all_friends = [friend, my_friends]

print(all_friends)

print(all_friends[1][0])

my_friends.append("Autum")
print(my_friends)

del my_friends[4]

print(my_friends)

print(len(all_friends))

all_friends_again = my_friends + friend
print(len(all_friends_again))

for i in reversed(friend):
    print(i)


for i in friend:
    print(i * 4)

for i in friend:
    if i == 'Joey':
        print("How you doing?")
    elif i == "Chandler":
        print("HAHAHAHAH")
    elif i == "Ross":
        print("Annoying")
    elif i == "Monica":
        print("Relatable")
    elif i == "Phoebe":
        print("Growing on me")
    elif i == "Rachael":
        print("Always seems to be cold")
    else:
        print(i)


super_heroes = {'Spider-Man' : 'Peter Parker',
                'Iron Man' : 'Tony Stark',
                'Batman' : 'Bruce Wayne'}

print(super_heroes['Batman'])

del super_heroes['Batman']

print(super_heroes)

super_heroes['Spider-Man'] = 'Miles Moralis'

print(super_heroes)

print(super_heroes.keys())

print(super_heroes.values())
