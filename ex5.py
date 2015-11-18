my_name = 'Kevin Yang'
my_age = 17 # not a lie
my_height = 171 # centimeters
my_weight = 60 # kilograms
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)