from sys import exit


def first_floor():
    print "There is the way to go the office"
    print "There is the way to go to the basement"
    print "There is the way to go to second floor"
    print "Where do you want to go?"

    choice = raw_input("> ")

    if choice == "go to the office":
        print "No one is there"
        office()

    elif choice == "go to the basement":
        print "All the SCS students and faculties are in chapel"
        basement()

    elif choice == "go to the second floor":
        print "There is the elementary school"
        second_floor()

    else:
        dead("You're kicked out of school!")


def office():
    print "Suddenly, two dogs are trying to attack you"
    print "What would you do with them?"

    choice = raw_input("> ")

    if choice == "run away":
        print "You just survived from the attack"
        first_floor()

    else:
        dead("They bite you")


def basement():
    print "Mr.Olinda comes and tells you to be in the chapel"
    print "What is your choice?"

    choice = raw_input("> ")

    if choice == "seat":
        print "Pastor Johnson is having his speech!"
        print "You just got message from him"
        print "You're saved!"
        print "Chapel just finished"
        first_floor()

    else:
        dead("Pastor Johnson just called your name!")


def second_floor():
    print "some elementary students are asking you to hang out with them."
    print "What are you going to do?"

    choice = raw_input("> ")

    if choice == "hang out":
        print "You just got extra points from elementary teachers."
        third_floor()

    else:
        dead("They start to cry, so teachers come out and you are in trouble")


def third_floor():
    print "The door is locked"
    print "Are you going to break the door or go up?"

    choice = raw_input("> ")

    if choice == "go up":
        print "You're in the roof"
        roof()

    else:
        dead("All the teachers are coming up because of you. You're doomed hahaha")


def roof():
    print "There is a helicopter waitin for you!"
    print "Are going to take in or just ignore?"

    choice = raw_input("> ")

    if choice == "take in":
        print "Welcome! you're in the special force from now on!"
        exit(0)

    else:
        dead("The building is just destroyed..")


def dead(why):
    print why, "I'm sorry, good bye"
    exit(0)

def start():
    print "You are in front of the SCS building"
    print "Do you want to go in or not?"

    choice = raw_input("> ")

    if choice == "Yes":
        first_floor()

    else:
        dead("You just got all F!")


start()
