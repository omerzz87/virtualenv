from icecream import ic

cars=[]

def menu():
    while True:
        print('welcome to the garage')
        print('"add" - add a car')
        print('"del"- Remove car')
        print('"p"- List the cars')
        print('"x"- Exit')
        choice = input('Enter your choice: ')

        if choice == "add":cars.append('Hyundai')
        elif choice == "del":cars.pop()
        elif choice == "p":ic(cars)
        elif choice == "x":exit()
        else:
            print('Invalid choice')
            
    



def main():
    menu()
if __name__ == '__main__':
    main()