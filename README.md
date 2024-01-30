# TSP Solver for DreamFlight Airline

This project provides a solution to the Traveling Salesman Problem (TSP) for DreamFlight Airline, optimizing the route for its flights. The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits a given set of cities and returns to the starting city. In this case, the cities represent airports, and the distances between them are calculated based on their geographical coordinates.

## TSP Solver Implementation

The TSP solver is implemented in `tsp.py` and consists of the following components:

### TSP Class

- `__init__(self, airports)`: Initializes the TSP solver with a dictionary of airport names and their corresponding geographical coordinates.

- `cities_connection(self)`: Generates a list of connections between pairs of airports.

- `haversine(self, list_of_connections)`: Calculates the distances between airport pairs using the Haversine formula.

- `calculate_total_distance(self, route)`: Calculates the total distance of a given route.

- `tsp_bruteforce(self)`: Implements a brute-force algorithm to find the optimal route and its distance.

- `distances_betw_each_city_from_tsp(self, tsp_route_result)`: Computes the distances between each pair of cities in the TSP route.

- `solve(self)`: Calls the `tsp_bruteforce` method to find the optimal route and returns the result.

## Example Usage in `main.py`

The main script `main.py` provides an example of using the TSP solver for DreamFlight Airline. It defines a set of airports, initializes the TSP solver, finds the optimal route, and displays relevant information. Additionally, it creates an animated visualization of the optimal route on a map using Matplotlib and Basemap.

## Employee Shift Optimization

The file `amount_of_employees.py` contains functions related to optimizing the shifts of pilots and flight attendants based on the TSP route. The optimization takes into account the average speed of planes, working hours for pilots and flight attendants, and the staffing requirements per flight.

### Functions:

- `time_of_one_flight(distance, aircraft_speed=800)`: Calculates the time needed for a flight, including departure and arrival time.

- `pilot_shift(d, shortest_route)`: Optimizes the shift schedule for pilots based on flight distances and returns the list of crew changes.

- `flight_attendant_shift(d, shortest_route)`: Optimizes the shift schedule for flight attendants based on flight distances and returns the list of crew changes.

- `display_info(list_of_crew_change, who)`: Displays information about crew changes, including the city and the total number of employees.

## Visualization

The script uses Matplotlib and Basemap to create an animated visualization of the optimal route on a world map. The map includes markers for airports, the optimal route, and additional information about the route and its distance.

## Example Output

After running `main.py`, the script will print the optimal route and its distance. It will also display information about crew changes for pilots and flight attendants, as well as an animated map showing the optimal route.

Feel free to customize the airports, add or remove airports for testing, and explore the optimization results for DreamFlight Airline.
