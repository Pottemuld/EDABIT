total_landmass = 148940000

def area_of_country(country, area):
    percentage = round((area / total_landmass) * 100, 2)

    print(country + " is " + str(percentage) + "% of the total world's landmass")

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)