colors = ["Red", "Green", "Blue", "Yellow"]

districts = {
    "Adilabad": ["Nirmal", "Komaram Bheem"],
    "Nirmal": ["Adilabad", "Mancherial"],
    "Mancherial": ["Nirmal", "Peddapalli"],
    "Peddapalli": ["Mancherial", "Karimnagar"],
    "Karimnagar": ["Peddapalli", "Rajanna"],
    "Rajanna": ["Karimnagar", "Siddipet"],
    "Siddipet": ["Rajanna", "Medak"],
    "Medak": ["Siddipet", "Sangareddy"],
    "Sangareddy": ["Medak", "Hyderabad"],
    "Hyderabad": ["Sangareddy", "Medchal"],
    "Medchal": ["Hyderabad"]
}

assignment = {}

def safe(district, color):
    for n in districts[district]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack():
    if len(assignment) == len(districts):
        return True

    district = [d for d in districts if d not in assignment][0]

    for color in colors:
        if safe(district, color):
            assignment[district] = color

            if backtrack():
                return True

            del assignment[district]

    return False

backtrack()

print("Telangana Map Coloring")
for district in assignment:
    print(district, "=", assignment[district])
