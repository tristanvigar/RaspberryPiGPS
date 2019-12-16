def load_cities_list():
    cities_list = []
    import os
    current_dir = os.getcwd()
    with open(current_dir + '/world_cities/worldcities.csv', 'r') as cities_file:
        for line in cities_file:
             cities_list.append(line.strip())
    return cities_list

print(load_cities_list())
