'''Santa Claus's elves 🧝🧝‍♂️ have found a bunch of mismatched magic boots in the workshop. Each boot is described by two values:

· type indicates if it's a left boot (I) or a right boot (R).
· size indicates the size of the boot.

Your task is to help the elves pair all the boots of the same size having a left and a right one. To do this, you should return a list of the available boots after pairing them.

Note: You can have more than one pair of boots of the same size!'''

def organizeShoes(shoes):
    sizes = {}

    for shoe in shoes:
        size = shoe['size']
        shoe_type = shoe['type']

        if size not in sizes:
            sizes[size] = {'I': 0, 'R': 0}

        sizes[size][shoe_type] += 1 

    result = []
    for size, count in sizes.items():
        pairs = min(count['I'], count['R'])  
        result.extend([size] * pairs) 

    return result

# min(a, b): Finds the smaller of two values (used to calculate the number of complete pairs possible).
# extend(list): Adds all elements from list to the original list (used to add all sizes with complete pairs to the result).

shoes1 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38},
    {'type': 'R', 'size': 42},
    {'type': 'I', 'size': 41},
    {'type': 'I', 'size': 42}
]
print(organizeShoes(shoes1))  # [38, 42]

shoes2 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38},
    {'type': 'I', 'size': 38},
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 38}
]
print(organizeShoes(shoes2))  # [38, 38]

shoes3 = [
    {'type': 'I', 'size': 38},
    {'type': 'R', 'size': 36},
    {'type': 'R', 'size': 42},
    {'type': 'I', 'size': 41},
    {'type': 'I', 'size': 43}
]
print(organizeShoes(shoes3))  # []
