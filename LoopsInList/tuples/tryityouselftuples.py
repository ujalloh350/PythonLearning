simple_food = ("rice and beans","soup","burger","pizza","desert")
updated_menu = list(simple_food)
updated_menu[1]="Chicken soup"
simple_food = tuple(updated_menu)

print("Original menu:")
for food in simple_food:
    print(food.title())

simple_food = ("ice cream","potato soup","cake")
print("\nThis is an updated menu:")
for food in simple_food:
    print(food.title())

cars =("bmw","audi","toyota")
print("\n update cars:")
updated_cars = list(cars)
updated_cars[0]="rover"
cars = tuple(updated_cars)
for car in cars:
    print(car.title())