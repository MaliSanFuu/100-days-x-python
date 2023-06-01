#dicts and nesting
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",

}
#Retriebing imtes from dictionary
print(programming_dictionary["Function"])
print("- - - - - - - - - - ")

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)
print("- - - - - - - - - - ")

empty = {}

#Wipe an existing dicitionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

print("- - - - - - - - - - ")

#loop through a dictionary
for key in programming_dictionary:
    print(key, programming_dictionary[key])

#Nesting
{
    "key" : ["List"],
    "key2": {"Dict"},
}

#Nesting List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germay": ["Berlin", "Hamburg", "Stuttgart"],
}
 
#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visisted": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visisted": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France", 
        "cities_visisted": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visisted": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]