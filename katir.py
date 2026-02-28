print(
    "Welcome!\n If this is your first time using the program, please use '2. Update'\n \
to update the directory of current open Kattis problems. Afterwards, I would\n \
recommend updating it every few weeks or once a month. It takes around 2-3 minutes.\n \
..."
)

while True:
    choice = input("Select an option (number): \n \
    1. Problem lookup\n \
    2. Update\n \
    3. Exit\n")

    if choice == '1':
        while True:
            import get_reservations  # Adds a slight delay, but it's to avoid the possibility of a wrong answer
            r = open('Reservations.txt')
            p = open('Problems.txt')
            reservations = r.read()
            problems = p.read()

            name = input("Enter the name of the problem (0 to go back): ")
            if name == '0':
                break
            
            if name in problems and name in reservations:
                print("This problem is ALREADY reserved!\n")
            elif name in problems and name not in reservations:
                print("This problem is NOT reserved!\n")
            elif name not in problems:
                print("This problem does not exist! Check your spelling and follow the lookup guide!\n")
    elif choice == '2':
        import get_problems
        print("The problem directory has been updated!\n")
    elif choice == '3':
        break
    else:
        print("Please enter a valid number!\n")
