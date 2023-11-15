
pets = []


pet = {
    'animal type': 'snake',
    'name': 'fluffy',
    'owner': 'hannah',
    'weight': 35,
    'eats': 'mouses',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'meowzer',
    'owner': 'lily',
    'weight': 29,
    'eats': 'tuna',
}
pets.append(pet)

pet = {
    'animal type': 'bunny',
    'name': 'terror',
    'owner': 'marlou',
    'weight': 23,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))