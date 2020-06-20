# First program to test. This will not be using VIM unfortunately


# for key in dictionary: (note that this only selects keys)

# dict.items() method
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('%s: %d' % (soda, calories))

# dict.keys() method
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)

# dict.values() method
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)

# list() to convert view objects into lists
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

closest = sorted(list_of_distances)[0]
next_closest = sorted(list_of_distances)[1]

print('Closest planet is %.4e' % closest)
print('Second closest planet is %.4e' % next_closest)

