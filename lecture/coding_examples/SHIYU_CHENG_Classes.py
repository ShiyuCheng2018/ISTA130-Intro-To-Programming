class Dog:
    def __int__(self, breed, name, age, weight):
        self.bread = breed
        self.name = name
        self.age = age
        self.weight = weight

    def __repr__(self):
        return f"----- Rocket -----\n  Breed: Australian Cattle Dog\n  Age: 8\n  Weight: 42.3 lbs."

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

def main():
    myDog = Dog("Fluffy", "Pikachu", 3, 30)
    otherDog = Dog("Hairless", "Jack", 4, 20)
    print(myDog.dogfight(otherDog))

if __name__ == '__main__':
    main()






