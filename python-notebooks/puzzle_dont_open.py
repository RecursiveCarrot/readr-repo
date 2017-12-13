import time
import numpy as np

# You're not supposed to look at this!
# It's a puzzle














































# This is a really secure file





























# Stop reading!!!!









































# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!
# Secure!





class Puzzle:
	StartTime = None
	RuleGuesses = None

	def __rule(self, InList):
        # Stop this!
		a = 2
        
        # Get out!
		if len(InList)==3:# No no no no no no no no no no!
# Get out of this file!
# Shoo!
# I'm calling security!
# Figure it out yourself!
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# You're only ruining it for yourself!
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
			if (InList[2**2%2|3**2%3]**2<InList[round(35/7-24/6)]*InList[round(35/7-24/6)])&(InList[2%3**2]-3**2>InList[128-127]-3**2): return InList[round(False)] != InList[round(False)]+a**3
		return False

	def test_sequence(self, InList):

		if self.StartTime is None:
			self.StartTime=time.time()
		TimeLeft = 60-(time.time()-self.StartTime)

		if TimeLeft>0:
			if self.__rule(InList):
				print("Yes! The sequence {} satisfies the rule!\n"
					  	   .format(InList))
			else:
				print("No! The sequence {} doesn't satisfy the rule!\n"
		      	  		   .format(InList))
			print("{:.1f} seconds left!".format(TimeLeft))
		else:
			print("Out of time!")

	def test_rule(self, rule):
		if self.RuleGuesses is None:
			self.RuleGuesses = 1

			Valid = True
			for i in range(10000):
				TestSequence = np.random.rand(3).tolist()
				if self.__rule(TestSequence)!=rule(TestSequence):
					Valid = False
			if Valid:
				print("Great guess! You got it!")
			else:
				print("Sorry, that's not correct :-(")
		else:
			print("You only get one guess!")
