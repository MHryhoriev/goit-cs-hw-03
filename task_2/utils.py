import re

def input_cat_name():
    """
    Prompts the user to input a valid cat name and returns the name.
    
    Returns:
        str: The cat's name entered by the user.
    """
    while True:
        cat_name = input("Please enter the cat's name (only letters and spaces allowed): ").strip()
        
        if not cat_name:
            print("Name cannot be empty. Please try again.")
            continue
        
        if not re.match("^[A-Za-zА-Яа-яІіЄєЇїҐґЄє ]+$", cat_name):
            print("Invalid name. Only letters and spaces are allowed. Please try again.")
            continue
        
        return cat_name


def input_cat_age():
    """
    Prompts the user to input a valid age for the cat and returns the age as an integer.
    
    Returns:
        int: The cat's age entered by the user as a positive integer.
    """
    while True:
        age_input = input("Please enter the cat's age (a positive integer): ").strip()
        
        if not age_input.isdigit() or int(age_input) <= 0:
            print("Invalid input. Please enter a positive integer for the age.")
            continue
        
        return int(age_input)
    
def input_new_feature():
    """
    Prompts the user to input a new feature for the cat and returns the feature as a string.
    
    Returns:
        str: The new feature for the cat entered by the user. 
    """
    while True:
        feature = input("Please enter a new feature for the cat (can include spaces and symbols): ").strip()
        
        if not feature:
            print("Feature cannot be empty. Please try again.")
            continue
        
        return feature