# main.py

from pet import Pet, Dog, Cat

def main():
    """
    Creates a Pet object and tests its methods.
    """

    # Create a generic Pet object
    my_pet = Pet("Buddy", "dog", 3)
    my_pet.display_info()
    my_pet.make_sound()
    print("-" * 20) # Separator

    #Create a Dog object
    my_dog = Dog("Charlie", 5, "Golden Retriever")
    my_dog.display_info()
    my_dog.make_sound()
    print("-" * 20) # Separator

    #Create a Cat object
    my_cat = Cat("Whiskers", 2, "White")
    my_cat.display_info()
    my_cat.make_sound()
    print("-" * 20) # Separator



if __name__ == "__main__":
    main()
