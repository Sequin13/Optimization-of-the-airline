from main import tsp_solver, shortest_route


#planes fly at an average speed of 800 km/h

#pilots can work for 6h a day -

#flight attendants can work 8h a day

#per flight we need 2 pilots and 3 flight attendant


print(shortest_route)

dic_of_routes_with_distances=tsp_solver.distances_betw_each_city_from_tsp(shortest_route)
d=dic_of_routes_with_distances

flight_attendant_counter=0

def time_of_one_flight(distance):
    time_int=distance/800
    minutes=int(time_int*60)

    return (minutes+60) #added 1h as a cost of departure and arrival

def pilot_shift():
    limit=6*60 #6h of pilot shift
    current_shift=0
    pilot_counter=2
    for key in d:

        if current_shift+time_of_one_flight(d[key])>limit:
            pilot_counter+=2
            current_shift=0
        print(current_shift, pilot_counter)
        current_shift = current_shift + time_of_one_flight(d[key])
    print()
    return pilot_counter


def flight_attendant_shit():
    limit=8*60 #8h of flight attendant shift
    current_shift=0
    fa_counter=3
    for key in d:

        if current_shift+time_of_one_flight(d[key])>limit:
            fa_counter+=3
            current_shift=0
        print(current_shift, fa_counter)
        current_shift = current_shift + time_of_one_flight(d[key])
    print()
    return fa_counter

print(pilot_shift())
print(flight_attendant_shit())