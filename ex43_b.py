class CentralCorridor(Scene):

    def enter(self):
        print """The lamias have attacking and killing people
so you should be the hero and save the world from lamias
that are spreading errors all over the world.
The goal for you is to kill all the lamias and to escape.
\nGood luck!\n"""
        print "One lamia has come upon you. How are you going to defeat it?"
        print """Actions:
            -With bear hand
            -Shoot a gun
            -Use the Christian Armor"""

        action = raw_input("> ")

        if action == "With bear hands":
            print """You are fast enough to dodge every attacks from the lamia
but soon you get tired and cannot attack the lamia with your bear hands!
The lamia had defeated you. He gave your body to its babies."""
            return 'death'

        elif action == "Shoot a gun":
            print """The lamia had dodged all the bullets that you had shot.
No more bullets!!! The lamia had killed you and gave your body
to its babies."""
            return 'death'

        elif action == "Use the Christian Armor":
            print """Even though, the Armor is inexperienced, you could defeat
one lamia. However, to kill more lamias you need
the perfect ChristianArmor."""
            return 'LWA'

        else:
            print "DOES NOT RECOGNIZE!"
            return 'cent.corri.'


class LaserWeaponArmory(Scene):

    def enter(self):
        print """You have successfully killed the lamia. However, you need a
holier Christian Armor. Lamia had stolen it from Arthur and kept it
in the Armory. Solve the question and get the Armor. You have 5 tries.
The question is:
Divide 20 by 1/2 and add 10."""
        answer = 50
        guess = int(input("> "))
        guesses = 0

        while guess != answer and guesses < 5:
            print "WRONG"
            guesses += 1
            guess = int(input(">"))

        if guess == answer:
            print """You are correct! There is the perfect holy Christian
Armor of Arthur. Now you can defeat all the lamias."""
            return 'bridge'

        else:
            print """The armory emits poison ous gas so you
suffocate and die."""
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print """Now you are carrying your perfect experienced Christian Armor.
So you came to the bridge where there are the most lamias which are
constantly spreading errors to the world.
You need to stop this immediately.
There are total 20 lamias. Choose the correct action to defeat them."""
        print """Actions:
            -Wear the perfect Christian Armor
            -Wear the inexperienced Armor"""

        action = raw_input("> ")

        if action == "Wear the perfect Christian Armor":
            print """You finally wore the perfect Christian Armor from Arthur.
Now you are holy enough to defeat all the lamias from the world.
Thank you for doing a great job."""
            return 'escape'

        elif action == "Wear the inexperienced Armor":
            print """You again wore the inexperienced Armor that you had hard
time fighting the first lamia. Now you do not have any more
strength to defeat rest of the lamias. The lamias have killed you
and are spreading more errors."""
            return 'death'
        else:
            print "DOES NOT RECOGNIZE!"
            return 'bridge'


class EscapePod(Scene):

    def enter(self):
        print """You have to choose the correct pod in order to escape safely.
        There are three types:gold, silver, and lead. The gold one said
        that a man would get what many men desire. The silver one said
        that a man would get what he deserved. The lead one said that
        a man would have to give and hazard all.
        Which one will you choose?"""

        choice = raw_input("> ")

        if choice == "gold":
            print """The outside of this pod looks nice and fancy but
            it could not function well. You have drowned and died."""
            return 'death'

        elif choice == "silver":
            print """Even though this one looks tempting, you are a fool.
            You will deserve death."""
            return 'death'

        elif choice == "lead":
            print """You had risked your life to save the world. Great job!
            I aprreciate your help to the world."""
            return 'finish'


class Finished(Scene):

    def enter(self):
        print """You have successfully defeated all the lamias
        and now the world is free from errors."""
        exit(0)
