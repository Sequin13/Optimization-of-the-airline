#planes fly at an average speed of 800 km/h

#pilots can work for 6h a day -

#flight attendants can work 8h a day

#per flight we need 2 pilots and 3 flight attendant


def time_of_one_flight(distance, aircraft_speed=800):
    time_int=distance/aircraft_speed
    minutes=int(time_int*60)

    return (minutes+60) #added 1h as a cost of departure and arrival

def pilot_shift(d, shortest_route): # d is a dictionary with flight connections and distance beetween itz
    list_of_pilot_change =[]
    limit=6*60 #6h of pilot shift
    current_shift=0
    pilot_counter=2
    for key in d:
        if current_shift+time_of_one_flight(d[key])>limit:
            for city in range(len(shortest_route)):
                if city + 1 < len(shortest_route) and shortest_route[city + 1]:
                    if shortest_route[city] in key and shortest_route[city+1] in key:
                        # print("Przesiadka w", shortest_route[city])
                        list_of_pilot_change.append(shortest_route[city])
            pilot_counter+=2
            current_shift=0
        current_shift = current_shift + time_of_one_flight(d[key])
    list_of_pilot_change.append(pilot_counter) #number of needed pilots is at the end of the list
    return list_of_pilot_change


def flight_attendant_shift(d, shortest_route):
    limit=8*60 #8h of flight attendant shift
    current_shift=0
    fa_counter=3 #fa stands for flight attendant
    list_of_fa_change=[]
    for key in d:
        if current_shift + time_of_one_flight(d[key]) > limit:
            for city in range(len(shortest_route)):
                if city + 1 < len(shortest_route) and shortest_route[city + 1]:
                    if shortest_route[city] in key and shortest_route[city + 1] in key:
                        list_of_fa_change.append(shortest_route[city])
            fa_counter+=3
            current_shift=0
        current_shift = current_shift + time_of_one_flight(d[key])
    list_of_fa_change.append(fa_counter)
    return list_of_fa_change

def display_info(list_of_crew_change, who):
    l=list_of_crew_change
    for i in range(len(l)-1):
        print("Wymiana załogi:",who, "w mieście", l[i])
    print("Łączna ilość pracowników -", who, ":",l[len(l)-1])