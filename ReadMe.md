# MY ANSWER

# Func Solution
def flatten_and_sort(arr):
    return sorted([elem for sublist in arr for elem in sublist])

# Test the function
input_list = [[3, 2, 1], [7, 8, 9], [4, 5, 6]]
result = flatten_and_sort(input_list)
print(result)

# Functional Prompt
# How does this solution ensure data immutability?
# This will ensures data immutability because it doesn't modify the original input list. It creates a new list without changing the og data.

# Is this solution a pure function? Why or why not?
# Pure function because it only depends on its input.

# Is this solution a higher order function? Why or why not?
# Not a higher-order function because it doesn't take arguments or return functions.

# Would it have been easier to solve this problem using a different programming style?
# No, since this simplifies the process and won't alter the og data.

# Why is functional programming a helpful paradigm when solving this problem?
# It keeps data safe and use pure functions, same presented to this problem.



-----------------


# Object-Oriented Solution
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"

# Test the classes
pod = Podracer(100, "perfect", 5000)
pod.repair()
print("Pod Condition:", pod.condition)

anakins_pod = AnakinsPod(150, "repaired", 8000)
anakins_pod.boost()
print("Anakin's Pod Max Speed:", anakins_pod.max_speed)

sebulbas_pod = SebulbasPod(120, "trashed", 4000)
other_pod = Podracer(200, "perfect", 6000)
sebulbas_pod.flame_jet(other_pod)
print("Other Pod Condition:", other_pod.condition)



# Object oriented Prompt
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# - Encapsulation:
#       Encapsulate data and behavior, hiding implementation detail.
# - Inheritance: 
#       AnakinsPod and SebulbasPod inherit attributes and methods from the base class Podracer.
# - Abstraction: 
#       The classes provide abstractions for working with podracer objects by defining methods like repair and boost.
# - Polymorphism:
#       Polymorphism is not demonstrated.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# For organizing and modeling, OOP is easier because it allows for clear structuring of data and behavior.

# How in particular did Object-Oriented Programming assist in the solving of this problem?
# OOP helps in modeling and organizing objects.

# Reflection
# Is one of these coding paradigms "better" than the other? Why or why not?
# Depends on goeal and problem presented.

# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
# If I'm working on data processing and transformation, functional programming might be more appealing. 
# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object-Oriented Programming?
# Functional programming is for data transformation, filtering, and mapping. OOP is for modeling and organizing objects with behaviors.

# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
# Both,it depends on one's background and experience and more practice is key. Working on projects that require each paradigm will help.



