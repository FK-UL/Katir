import pickle


print('Welcome to Katir!')  # Refresh reservations upon each launch to ensure functionality (adds 1-2s delay)
import get_reservations
with open("Reservations.pkl", "rb") as r:
    reservations = pickle.load(r)


try:  # Loads the problems dataset, if not present, generates it anew
    with open("Problems.pkl", "rb") as p:
        problems = pickle.load(p)
except:
    print('Could not find directory of available problems. Updating, please wait...')
    print('(Takes around 2-3 minutes, depending on network speed.)')
    import get_problems
    with open("Problems.pkl", "rb") as p:
        problems = pickle.load(p)

try:
    choice = int(input('Select an option:\n \
          1. Available problems by difficulty\n \
          2. Check problem availability\n \
          3. Update problem directory\n'))
except:
    print('That is not a valid number!')


if choice == 1:
    print('Select the difficulty range you want to get\n\
          available problems for (format: X Y (decimals allowed))')
    numbers = input().split()
    lower_bound = numbers[0]
    upper_bound = numbers[1]  # This part can fail if the input does not have an empty space

    try:
        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
    except:
        print('Invalid input!')
    
    avail = []
    for problem, difficulty in problems.items():
        if problem not in reservations and lower_bound <= difficulty <= upper_bound:
            avail.append((difficulty, problem))
    
    for dif, pro in sorted(avail):  # We save the pairs in a list, and print them out by order of difficulty
        print(f'{pro}: {dif}T')
    

elif choice == 2:    
    name = input("Enter the name of the problem:\n")

    if name in problems and name in reservations:
        print(f"{name} is ALREADY reserved!\n")
    elif name in problems and name not in reservations:
        print(f"{name} is NOT reserved!\n")
    elif name not in problems:
        print("This problem does not exist! Check your spelling and follow the lookup guide!\n")

elif choice == 3:  # Updates the problems database.
    import get_problems