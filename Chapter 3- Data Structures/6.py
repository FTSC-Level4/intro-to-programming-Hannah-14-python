guests = ['Spongebob Square Pants', 'Dan Heng', 'Marty Buer']

name = guests[0].title()
print(name + ", would you like to come for dinner.")

name = guests[1].title()
print(name + ", would you like to come for dinner.")

name = guests[2].title()
print(name + ", would you like to come for dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[1])
guests.insert(1, 'Jeff')

name = guests[0].title()
print("\n" + name + ", would you like to come for dinner.")

name = guests[1].title()
print(name + ", would you like to come for dinner.")

name = guests[2].title()
print(name + ", would you like to come for dinner.")

print("\nWe got a bigger table!")
guests.insert(0, 'dr. ratio')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")
