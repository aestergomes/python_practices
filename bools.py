# compare the population density of San Francisco and Rio de Janeiro.
# print True if the density of San Francisco is higher, otherwise print False.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)