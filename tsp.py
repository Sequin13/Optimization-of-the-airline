import numpy as np
from itertools import permutations

class TSP:
    def __init__(self, airports):
        self.airports = airports
        self.distances = self.haversine(self.cities_connection())

    def cities_connection(self):
        list_of_connections = []
        for city in self.airports.keys():
            for city2 in self.airports.keys():
                if city < city2:
                    list_of_connections.append((city, self.airports[city], city2, self.airports[city2]))
        return list_of_connections

    def haversine(self, list_of_connections):
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

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            key_forward = f'{route[i]} - {route[i + 1]}'
            key_backward = f'{route[i + 1]} - {route[i]}'
            if key_forward in self.distances:
                total_distance += self.distances[key_forward]
            elif key_backward in self.distances:
                total_distance += self.distances[key_backward]

        key_return = f'{route[-1]} - {route[0]}'
        if key_return in self.distances:
            total_distance += self.distances[key_return]

        return total_distance

    def tsp_bruteforce(self):
        cities = set()
        for key in self.distances:
            cities.update(key.split(' - '))

        shortest_route = None
        shortest_distance = float('inf')

        for route_permutation in permutations(cities):
            route_permutation += (route_permutation[0],)
            total_distance = self.calculate_total_distance(route_permutation)

            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_route = route_permutation

        return shortest_route, shortest_distance

    def distances_betw_each_city_from_tsp(self, tsp_route_result):
        dic_of_tsp_each_distances = {}
        for i in range(len(tsp_route_result) - 1):
            city1, city2 = tsp_route_result[i], tsp_route_result[i + 1]
            key_forward = f'{city1} - {city2}'
            key_backward = f'{city2} - {city1}'

            if key_forward in self.distances:
                dic_of_tsp_each_distances[key_forward] = self.distances[key_forward]
            elif key_backward in self.distances:
                dic_of_tsp_each_distances[key_backward] = self.distances[key_backward]

        return dic_of_tsp_each_distances

    def solve(self):
        return self.tsp_bruteforce()
