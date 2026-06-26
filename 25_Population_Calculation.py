population = 10000
years = 10
for year in range(years, 0, -1):
    print(f"{year}th year - {int(population)}")
    population = population*0.9 