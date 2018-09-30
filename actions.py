# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Mariam Ali"
my_age = 22
my_bio = "Computer Engineer"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    exit = False
    while exit != True:
        print ()
        option = input("Would you like to: \n 1) Create a new club \n 2) Browse and join clubs \n 3) View existing clubs \n 4) Display members of a club\n-1) Close application \n")

        if option == "1":
            create_club()
        elif option == "2":
            join_clubs()
        elif option == "3":
            view_clubs()
        elif option == "4":
            view_club_members()
        elif option == "-1":
            exit = True
        else:
            print ("invalid input please try again!")

def create_club():
    # your code goes here!
    name = input("Pick a name for your new club: \n")
    des = input("What is your club about? ")
    newClub = Club(name, des)
    print()
    for p in population:
        print ("[" + str(population.index(p)) + "]" + p.name)

    print()
    num = input("Please enter the number of the person you'd like to recruit to your new club or '-1' to stop: \n")
    #print ("----------------------------------------------------------------------------------")
    while num != "-1":
        if int(num) < len(population):
            newClub.recruit_member(population[int(num)])
            num = input()
        else:
            print ("Invalid number please try again:")
            num = input()

    newClub.recruit_member(myself)
    newClub.assign_president(myself)
    print ("Here's your club: \n")
    print (newClub)
    newClub.print_member_list()
    clubs.append(newClub)

def view_clubs():
    # your code goes here!
    for c in clubs:
        print ()
        print (c)

    print()

def view_club_members():
    #  your code goes here!
    view_clubs()
    clubName = input("Please enter the name of the club whose members you'd like to see: \n")
    for c in clubs:
        if clubName.lower() == c.name.lower():
            c.print_member_list()

def join_clubs():
    # your code goes here!
    view_clubs()
    ch = input("Enter the name of the club you'd like to join:\n")
    exit = False
    while exit != True:
        for c in clubs:
            if ch.lower() == c.name.lower():
                c.recruit_member(myself)
                print("\n%s just joined %s " %(my_name, c.name))
                exit = True

        if exit != True:
            ch = input("Invalid input please try again: \n")

def application():
    introduction()
    # your code goes here!
    options()
    




