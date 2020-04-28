'''
Prompt: Write an instance method called dogfight that takes another Dog object as an argument. If one of the dogs is at least 10 years old and the other is less than 10, the younger dog wins. Otherwise, the heavier dog wins. If they have the same weight, return 'Tie'. Return the name of the dog that wins.

All Dog objects have instance variables - breed, name, age, and weight. Just like when we use 'self' to refer to the unborn instance of the class, we can use 'other' (for the other dog) to reference an unborn separate instance of the class.
'''

def dogfight(self, other):
	'''
	Self refers to the instance we're calling dogfight on (one of the dogs, the unborn instance of the class).
	Other *also* refers to another instance of the Dog class. It has all instance variables and methods that 'self' has. This means we can reference the instance variables that are relevant (other.name, other.age and other.weight) that are relevant! All you have to do from there is compare the two.
	'''
	if self.age >= 10 and other.age < 10:
		# other is younger, so other wins
		return other.name
	if self.age < 10 and other.age >= 10:
		# self is younger, so self wins
		return self.name
	#From there, we move into determining the winner by
	#weight since their ages are not different enough.
	if self.weight > other.weight:
		# self is heavier, so self wins
		return self.name
	if other.weight > self.weight:
		# other is heavier, so other wins
		return other.name
	#If we made it here, that means we have a tie! So!
	return 'Tie'