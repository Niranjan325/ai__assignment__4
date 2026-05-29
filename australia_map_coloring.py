colors = ["Red", "Green", "Blue"]

states = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

assignment = {}

def is_safe(state, color):
    for neighbor in states[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve():
    if len(assignment) == len(states):
        return True

    unassigned = [s for s in states if s not in assignment]
    state = unassigned[0]

    for color in colors:
        if is_safe(state, color):
            assignment[state] = color

            if solve():
                return True

            del assignment[state]

    return False

solve()

print("Australia Map Coloring Solution")
for state in assignment:
    print(state, "=", assignment[state])
