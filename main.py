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
		pass


class BookRoomHaHa(Room):
	def book(self):
		print "ok, you ate the book."

	def bookviewing(self):
		print "you're in a room. who knows what kind yet?"
		print "so what do you do?"
		get_it_done = raw_input("> ")

		if "book" in get_it_done:
			print "ok booktest go"
			self.book()
			#from stackoverflow
			# http://stackoverflow.com/questions/5615648/python-call-function-within-class
		elif "shelf" in get_it_done:
			print "you see a few books I guess, I don't know, man!"
		elif "thing2" in get_it_done:
			print "thing 2"
		else:
			print "try again doof"


class DontDoIt(Room):
	pass

crum = BookRoomHaHa()
crum.bookviewing()
