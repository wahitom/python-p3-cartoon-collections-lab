dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
def roll_call_dwarves(dwarves):
    print("\n".join([f"{i}. {dwarf}" for i, dwarf in enumerate(dwarves, start = 1)]))
roll_call_dwarves(dwarves)


planeteer_calls = ["earth", "wind", "fire", "water"]
def summon_captain_planet(list_calls):
    for call in list_calls:
        print(call.capitalize() + "!")

    return list_calls
summon_captain_planet(planeteer_calls)


short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(list):
    if len(list) == 4:
        print(True)
        return True
    elif len(list) != 4:
        print(False)
        return False

long_planeteer_calls(short_words)
long_planeteer_calls(assorted_words)

cheeses = ["cheddar", "gouda", "camembert"]
snacks = ["crackers", "gouda", "thyme"]
soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]

def find_the_cheese(item_list):
    for cheese in cheeses:
        if cheese in item_list:
            print(cheese)
            return cheese
    print(None)
    return None

find_the_cheese(snacks)
    
