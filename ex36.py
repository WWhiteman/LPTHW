from sys import exit

def first_room():

	print "You come through a door into the first room."
	print "You see a dragon blocking the door."
	print "What do you do?"
	print "Tickle the dragon with a feather?"
	print "Yell at the dragon to get the fuck out?"
	print "Patiently wait until the dragon falls asleep?"
	next = ""
	next = raw_input()

	if "tickle" in next:
		dead("The dragon ROFL's then stomps you into a puddle of flesh.")
	elif "fuck" in next:
		print "The dragon looks shocked and quickly steps out of the way."
		second_room()
	elif "wait" in next:
		dead("You wait until you die.")
	else:
		print "Do something smart."
		first_room()


def second_room():

	print "You come through a door into the second room."
	print "You see nothing in the room but a door on the other side."
	print "What do you do?"
	print "Walk calmly over and go through the door?"
	print "Edge around the side of the room to avoid traps?"
	print "Sprint to the door before anything happens?"

	next = ""
	next = raw_input()

	if "walk" in next:
		print "Nothing happens and you gain your freedom, you win!"
		exit(0)
	elif "edge" in next:
		dead("A blade comes out of the wall and cuts off your head")
	elif "sprint" in next:
		dead("The force of your feet cause a trapdoor to open, you die.")
	else:
		print "That doesn't make sense."
		first_room()


def dead(why):
	print "--------------------"
	print why, "Try again!"
	print "--------------------"
	first_room()

def start():
	first_room()

start()