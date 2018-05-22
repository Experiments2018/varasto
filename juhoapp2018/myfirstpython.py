price_per_square = 100
garden_price = 1000
super_price_per_square = 200


def house_price(lenght, width):
    space = lenght * width
    return space * price_per_square

def elite_house_price(lenght, width):
    space = lenght * width
    return space * price_per_square+garden_price

def super_house_price(lenght, width):
    space = lenght * width
    return space * super_price_per_square+garden_price

my_house_price = house_price(10,20)
trump_house_price = elite_house_price(100,200)
kim_house_price = super_house_price(100,200)

print('My house', my_house_price)
print('Trump', trump_house_price)
print('the Great Leader', kim_house_price)

a=[(10,20), (20, 30), (30,35)]
b=[house_price(i[0],i[1]) for i in a]
print(b)
