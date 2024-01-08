
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import permutations
from matplotlib.animation import FuncAnimation

airports = {
    "Katowice": (50.4745, 19.0808),
    "London": (51.4694, -0.4474),
    "Paris": (49.0097, 2.5479),
    "Reykjavik": (63.9850, -22.6051),
    "Oslo": (60.1976, 11.1004),
    "Ankara": (40.1289, 32.9959)
}


def cities_connection(cities):
    list_of_connections = []
    for city in cities.keys():
        for city2 in cities.keys():
            if city < city2:
                list_of_connections.append((city, cities[city], city2, cities[city2]))
    return list_of_connections


def haversine(list_of_connections):
    dic = {}
    for i in range(len(list_of_connections)):
        lat1 = list_of_connections[i][1][0]
        lon1 = list_of_connections[i][1][1]
        lat2 = list_of_connections[i][3][0]
        lon2 = list_of_connections[i][3][1]

        con = list_of_connections[i][0] + " - " + list_of_connections[i][2]

        dLat = (lat2 - lat1) * np.pi / 180.0
        dLon = (lon2 - lon1) * np.pi / 180.0
        lat1 = (lat1) * np.pi / 180.0
        lat2 = (lat2) * np.pi / 180.0

        a = (np.sin(dLat / 2) ** 2 +
             np.sin(dLon / 2) ** 2 *
             np.cos(lat1) * np.cos(lat2))
        rad = 6371
        c = 2 * np.arcsin(np.sqrt(a))
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


def draw_shortest_route(frame):
    plt.clf()
    m = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=75,
                llcrnrlon=-30, urcrnrlon=60, resolution='c')
    m.drawcoastlines()
    m.drawcountries()

    route_coordinates = [airports[city] for city in shortest_route[:frame+1]]
    route_coordinates = np.array(route_coordinates)

    x, y = m(route_coordinates[:, 1], route_coordinates[:, 0])
    m.plot(x, y, 'mo--', markersize=10, linewidth=2)

    for city, coordinates in airports.items():
        x, y = m(coordinates[1], coordinates[0])
        m.plot(x, y, 'ro', markersize=8)
        plt.text(x, y, city, fontsize=12, ha='left', color = 'blue')

    plt.title(f'Optimal route for DreamFlight airline')
    plt.axis('off')
    plt.subplots_adjust(bottom=0.1)
    shortest_route_str=""
    for airport in shortest_route:
        shortest_route_str+=airport+" - "
    shortest_route_str = shortest_route_str[:-2]
    plt.text(0.5, -0.05, f'Shortest route: {shortest_route_str}', fontsize=12, ha='center', transform=ax.transAxes)
    plt.text(0.5, -0.09, f'Shortest distance: {shortest_distance} km', fontsize=12, ha='center', transform=ax.transAxes)


distances = haversine(cities_connection(airports))
shortest_route, shortest_distance = tsp_bruteforce(distances)

print("Najkrótsza trasa:", shortest_route)
print("Najkrótsza odległość:", shortest_distance)

fig, ax = plt.subplots(figsize=(12, 10))
ani = FuncAnimation(fig, draw_shortest_route, frames=len(shortest_route), interval=200, repeat=True)

plt.show()

