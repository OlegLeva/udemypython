states_needed = ["mt", "wa", "or", "id", "nv", "ut", "са", "az"]
states_needed = set(states_needed)

stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "са"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}
print(stations)
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        print(f'{covered} covered 1')
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            print(f'{covered} covered 2')
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)

