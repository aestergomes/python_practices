# You can create lists very quickly and concisely 
# with list comprehensions. This previous example:

# capitalized_cities = []
# for city in cities:
#    capitalized_cities.append(city.title())

# Can be reduced to:
cities = ['new york city', 'chicago', 'los angeles']
capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

# More examples:
# squares = [x**2 for x in range(9) if x % 2 == 0]

# squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]