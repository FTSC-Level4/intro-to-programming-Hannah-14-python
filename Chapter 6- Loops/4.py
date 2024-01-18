sandwich_orders = [
    'turkey', 'roast beef', 'pastrami',
    'veggie', 'grilled cheese']
finished_sandwiches = []

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")