#players
players = ["charles","martina","micheal","florence","eli"]
print(players[-3:])

#looping list
players = ["charles","martina","micheal","florence","eli"]
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_food = ["pizza","falafel","carrot cake"]
my_food.append("cannoli")

friend_foods = my_food[:]
friend_foods.append("ice cream")

print("my favorite food are:")
print(my_food)
print("\nMy friend's favorite foods are:\n")
print(friend_foods)

my_cars = ["bmw","audi","toyota","bugatti"]
myfriends_cars = my_cars[:1]

print("my favorite car are: ")
print(my_cars)
print("my friend's cars are :")
print(myfriends_cars)