import math
from itertools import permutations

airports = {
    "Katowice": (50.4745, 19.0808),
    "London": (51.4694, -0.4474),
    "Paris": (49.0097, 2.5479),
    "Reykjavik": (63.9850, -22.6051),
    "Oslo": (60.1976, 11.1004),
    "Ankara": (40.1289, 32.9959)
}

def cities_connection(cities):
    list_of_connections=[]
    for city in cities.keys():
        for city2 in cities.keys():
            if city < city2:
                list_of_connections.append((city, cities[city], city2, cities[city2]))
    # print(list_of_connections)
    return list_of_connections

cities_connection(airports)

def haversine(list_of_connections):
    dic = {}
    for i in range(len(list_of_connections)):
        lat1 = list_of_connections[i][1][0]
        lon1 = list_of_connections[i][1][1]
        lat2 = list_of_connections[i][3][0]
        lon2 = list_of_connections[i][3][1]

        con = list_of_connections[i][0] + " - " + list_of_connections[i][2]

        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0

        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        dic[con] = round(rad * c)
    return dic

def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        key_forward = f'{route[i]} - {route[i + 1]}'
        key_backward = f'{route[i + 1]} - {route[i]}'
        if key_forward in distances:
            total_distance += distances[key_forward]
        elif key_backward in distances:
            total_distance += distances[key_backward]

    key_return = f'{route[-1]} - {route[0]}'
    if key_return in distances:
        total_distance += distances[key_return]

    return total_distance

def tsp_bruteforce(distances):
    cities = set()
    for key in distances:
        cities.update(key.split(' - '))

    shortest_route = None
    shortest_distance = float('inf')

    for route_permutation in permutations(cities):
        route_permutation += (route_permutation[0],)
        total_distance = calculate_total_distance(route_permutation, distances)

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = route_permutation

    return shortest_route, shortest_distance



distances = haversine(cities_connection(airports))
# for i in distances.items():
#     print(i)

shortest_route, shortest_distance = tsp_bruteforce(distances)
print("Najkrótsza trasa:", shortest_route)
print("Najkrótsza odległość:", shortest_distance)

