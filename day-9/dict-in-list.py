travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5,
    },
]

print(travel_log)
print("- - - - - - ")

def add_travel_country(country_visited, times_visited, citites_visited):
    new_entry = {}
    new_entry = {
            "country" : country_visited,
            "cities_visited" : citites_visited,
            "total_visits" : times_visited
        }
    travel_log.append(new_entry)

add_travel_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

for entry in travel_log:
    print(entry)