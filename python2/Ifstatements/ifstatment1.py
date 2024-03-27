#cars.py
cars =["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

request_topping ="mushrooms"
if request_topping != "anchovies":
    print("Hold the anchovies!")