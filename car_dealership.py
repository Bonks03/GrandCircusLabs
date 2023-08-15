trucks = {}
bikes = {}
vehicles_to_compare = {}

class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        return ('Beep Beep!')


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False
        trucks[make] = [miles, price]


    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed
        bikes[make] = [miles, price, top_speed]
        

    def make_noise(self):
        return ('Vroom Vroom!')

# Creating the objects. Only naming 2 of them to reference for noise
m1 = Motorcycle('Harley', 20000, 35750, 120)
Motorcycle('Ducatti', 4000, 42670, 250)
Motorcycle('Suzuki', 1000, 50000, 200)
t1 = Truck('F-150', 80000, 21000)
Truck('Ram 1500', 22000, 25510)
Truck('Raptor', 200, 56790)

if __name__ == '__main__':
    print('Welcome to GC Bike and Truck dealership!')
    
    # Takes user input, prints choices
    while True:
        view_choice = input('Would you like to view bikes or trucks? (b or t) \n> ')
        
        if view_choice.lower() == 'b' or view_choice.lower() == 'bikes':
            i = 1
            # This will help make the input for vehicles_to_compare easier
            view_choice = 'b'
            for bike in bikes:
                print(f'{i}. {bike}: with {bikes[bike][0]} miles and a ' 
                    f'top speed of {bikes[bike][2]} costs ${bikes[bike][1]}')
                i += 1

        elif view_choice.lower() == 't' or view_choice.lower() == 'trucks':
            i = 1
            # This will help make the input for vehicles_to_compare easier
            view_choice = 't'
            for truck in trucks:
                print(f'{i}. {truck}: with {trucks[truck][0]} miles ' 
                    f'costs ${trucks[truck][1]}')
                i += 1
        
        # Asks user to compare vehicles, if yes, adds their choice to list
        while True:
            compare = input('Would you like to compare one of these vehicles today? (y or n) \n> ')

            if compare.lower() == 'y' or compare.lower() == 'yes':
                index = input('Which vehicle would you like to compare? (please list number) \n> ')
                # Validate/sanitize user input.
                # If check is passed make will be added to vehicles_to_compare
                try:
                    index = int(index) - 1
                    if view_choice == 't' and index > (len(trucks.keys()) - 1):
                        raise ValueError
                    elif view_choice == 'b' and index > (len(bikes.keys()) - 1):
                        raise ValueError
                # Value error is raised if input not int or input too high
                except ValueError:
                    print('Invalid entry. please try again. Please only input a number.')
                # Adds user choice to dictionary, removes it as a future choice
                else:
                    if view_choice == 'b':
                        choice = list(bikes.keys())[index]
                        vehicles_to_compare[choice] = (bikes[choice], 'b') 
                        print(f'{choice} added!')
                        del bikes[choice]
                    elif view_choice == 't':
                        choice = list(trucks.keys())[index]
                        vehicles_to_compare[choice] = (trucks[choice], 't') 
                        print(f'{choice} added!')
                        del trucks[choice]
                    break
            
            elif compare.lower() == 'n' or compare.lower() == 'no':
                break
        
        # Adding this so the user chooses 2 or more vehicles to compare
        # Would be silly to compare just 1 vehicle since all info is already given
        if len(vehicles_to_compare) >= 2:
            while True:
                compare = input('Would you like to compare your vehicles now? (y or n) \n> ')
                if compare.lower() == 'y' or compare.lower() == 'yes':
                    print('Here are your vehicles to compare:')
                    print(vehicles_to_compare)
                    j = 1
                    for vehicle in vehicles_to_compare.keys():
                        print(f' {j} - {vehicle}: with {vehicles_to_compare[vehicle][0][0]} miles costs '
                                  f'${vehicles_to_compare[vehicle][0][1]}')
                        if vehicles_to_compare[vehicle][1] == 'b':
                            print(f'   {m1.make_noise()}')
                        elif vehicles_to_compare[vehicle][1] == 't':
                            print(f'   {t1.make_noise()}')
                        j += 1

                    done = True
                    break
                elif compare.lower() == 'n' or compare.lower() == 'no':
                    done = False                    
                    break

            if done:
                break
    while True:
        purchase = input('Would you like to buy one of these vehicles? (y or n) \n> ')
        if purchase.lower() == 'y' or purchase.lower() == 'yes':
            purchase_choice = input('Which vehicle would you like to purchase? (Please enter number) \n> ')
            # Validate/sanitize user input.
            # If check is passed user will purchase car.
            try:
                purchase_choice = int(purchase_choice) - 1
            except ValueError:
                print('Invalid entry. please try again. Please only input a number.')
            # Allows user to purchase the vehicle of their choice
            else:
                buy_choice = list(vehicles_to_compare.keys())[purchase_choice]
                print(f'{buy_choice} is ${vehicles_to_compare[buy_choice][0][1]}')
                buying = input('Are you sure this is the one you want? (y or n) \n> ')
                if buying == 'y' or buying == 'yes':
                    print('Thank you from purchasing from GC dealership! Have a nice day')
                    break
                else:
                    print("No worries, let's try again.")

        else:
            print('Thank you and have a nice day!')
            break                    