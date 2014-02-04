# first game maybe

class Room(object):

	def __init__(self):
		#self.name = name
		### doooon't get it here
		#self.foo = thing1
		#self.bar = thing2
		# these are placeholdery, I feel like putting "pass"
		# in the __init__ fn would be a bad time at this juncstuah
		# zed did also say to not put too much in the __init__
		# ... so what DO I put into it
		pass

class Inventory(Room):
	#why am I calling Room?  hmmm bc you have to be IN the room
	#to instantiate the Inventory class, maybe?
	#ok but all in all this class is looking better, if
	#only I could just GET to it, esp now that I've got the
	#invlist as part of the megafauna!

	def inventorycheck(self):
		print "inventory:\n %s" % invlist

	def inventoryadd(self, addnew):
		#don't know if putting var addnew in here is necessary right now
		if addnew in invlist:
			print "can't have more than one, homes"
		elif addnew not in invlist:
			print "cool!  now the %s is in your inventory." %addnew
			invlist.append(addnew)
			print "want to see what's in the bag now?"
			invchk = raw_input("> ")
			if 'y' in invchk:
				self.inventorycheck()
			elif 'n' in invchk:
				print "ok you don't have to, anyway it's over now"
				exit(0)
		else:
			print "error in adding item to inventory"	


class BookRoomHaHa(Room):
	def book(self):
		print "ok, you ate the book."
		exit(0)

	def bookviewing(self):
		print "you're in a room. who knows what kind yet?"
		print "so what do you do?"
		get_it_done = raw_input("> ")

		if "book" in get_it_done:
			# want to make this more abstractly, like, if VAR in get_it_done
			# then do some kind of "do you or don't you" inv taking action
			print "ok booktest go"
			self.book()
			#from stackoverflow
			# http://stackoverflow.com/questions/5615648/python-call-function-within-class
		elif "shelf" in get_it_done:
			print "you see a few books I guess, I don't know, man!"
		elif "thing2" in get_it_done:
			print "thing 2"
		elif "get" in get_it_done:
			print "buddy, you got it."
			print "for now, just tell me what you got, again: "
			addnew = raw_input("> ")
			#print "oktest!"
			# ok this piece is fine, now how to jump from one class
			# to another
			# why not just:
			#Inventory.inventoryadd()
			# doesn't work woh wohhhh
		else:
			print "try again doof"
			self.bookviewing()


class DontDoIt(Room):
	pass

invlist = []
crum = BookRoomHaHa()
crum.bookviewing()
