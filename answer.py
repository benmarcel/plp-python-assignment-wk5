# Superhero Class with Inheritance and Polymorphism

class Superhero:
    """
    Represents a superhero with a name, superpower, and weakness.
    This is the base class.
    """
    def __init__(self, name, superpower, weakness):
        """
        Constructor to initialize a Superhero object with unique values.
        """
        self.name = name
        self.superpower = superpower
        self.weakness = weakness

    def display_info(self):
        """
        Prints the superhero's information.
        """
        print(f"--- Superhero Info ---")
        print(f"Name: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Weakness: {self.weakness}")

    def use_superpower(self):
        """
        A method to demonstrate the superhero's action.
        This is the base class's implementation.
        """
        print(f"{self.name} uses their superpower: {self.superpower}!")

class TelepathicHero(Superhero):
    """
    Represents a telepathic hero. This class inherits from Superhero.
    It adds a new attribute and overrides the use_superpower method.
    """
    def __init__(self, name, superpower, weakness, telepathy_range):
        """
        Initializes a TelepathicHero object, calling the parent's constructor
        and adding a new attribute.
        """
        # Call the constructor of the parent class (Superhero)
        super().__init__(name, superpower, weakness)
        # Add a new, specific attribute for this subclass
        self.telepathy_range = telepathy_range

    def use_superpower(self):
        """
        Polymorphism in action! This method overrides the parent's
        use_superpower() method to provide a unique action.
        """
        print(f"{self.name} is reading minds from up to {self.telepathy_range} meters away!")

# ---

# Activity 2: Polymorphism Challenge

class Vehicle:
    """
    A base class for all vehicles.
    """
    def __init__(self, name):
        self.name = name

    def move(self):
        """
        The common method that will be implemented differently by each subclass.
        This base method is a placeholder.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    """
    A specific type of vehicle that moves by driving.
    """
    def move(self):
        """
        Polymorphic implementation of the move() method.
        """
        print(f"{self.name} is Driving!")

class Plane(Vehicle):
    """
    A specific type of vehicle that moves by flying.
    """
    def move(self):
        """
        Polymorphic implementation of the move() method.
        """
        print(f"{self.name} is Flying! ✈️")

def move_vehicles(vehicles):
    """
    A function that demonstrates polymorphism by iterating through a list of
    different vehicle types and calling their common move() method.
    """
    print("\n--- Polymorphism Challenge ---")
    for vehicle in vehicles:
        vehicle.move()

# Main program execution
if __name__ == "__main__":
    # Create instances of the classes for Activity 1
    print("--- Activity 1: Superhero Demonstration ---")
    superman = Superhero("Superman", "Flight and super strength", "Kryptonite")
    professor_x = TelepathicHero("Professor X", "Telepathy", "His own physical health", 1000)

    # Call methods on the objects
    superman.display_info()
    superman.use_superpower()
    print("-" * 20)
    professor_x.display_info()
    professor_x.use_superpower()
    print("-" * 20)

    # Create instances for Activity 2 and put them in a list
    my_car = Car("Ford Mustang")
    my_plane = Plane("Boeing 747")
    
    fleet = [my_car, my_plane]
    
    # Call the polymorphic function
    move_vehicles(fleet)
