import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
from tsp import TSP

airports = {
    "Katowice": (50.4745, 19.0808),
    "London": (51.4694, -0.4474),
    "Paris": (49.0097, 2.5479),
    "Reykjavik": (63.9850, -22.6051),
    "Oslo": (60.1976, 11.1004),
    "Ankara": (40.1289, 32.9959)
}

tsp_solver = TSP(airports)
shortest_route, shortest_distance = tsp_solver.solve()

print("Najkrótsza trasa:", shortest_route)
print("Najkrótsza odległość:", shortest_distance)

# #temporary
x=tsp_solver.distances_betw_each_city_from_tsp(shortest_route)
print(x)
#/temporary
fig, ax = plt.subplots(figsize=(12, 10))

def draw_shortest_route(frame):
    plt.clf()
    m = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=75,
                llcrnrlon=-30, urcrnrlon=60, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    route_coordinates = [airports[city] for city in shortest_route[:frame + 1]]
    route_coordinates = np.array(route_coordinates)

    x, y = m(route_coordinates[:, 1], route_coordinates[:, 0])
    m.plot(x, y, 'mo--', markersize=10, linewidth=2)

    for city, coordinates in airports.items():
        x, y = m(coordinates[1], coordinates[0])
        m.plot(x, y, 'ro', markersize=8)
        plt.text(x, y, city, fontsize=12, ha='left', color='blue')

    plt.title(f'Optimal route for DreamFlight airline')
    plt.axis('on')
    plt.subplots_adjust(bottom=0.1)
    shortest_route_str = ""
    for airport in shortest_route:
        shortest_route_str += airport + " - "
    shortest_route_str = shortest_route_str[:-2]
    plt.text(0.5, -0.05, f'Shortest route: {shortest_route_str}', fontsize=12, ha='center', transform=ax.transAxes)
    plt.text(0.5, -0.09, f'Shortest distance: {shortest_distance} km', fontsize=12, ha='center', transform=ax.transAxes)

ani = FuncAnimation(fig, draw_shortest_route, frames=len(shortest_route), interval=400, repeat=False)
plt.show()
