from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database
import json
from config import MONGO_URI

def get_db_connection():
    """Connects to the MongoDB and returns the database instance.
    
    Returns:
        db: The connected database instance, or None if the connection fails.
    """
    try:
        client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
        db = client.book
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def format_result(result):
    """Formats the result as a JSON string.
    
    Args:
        result (dict): The result to format.
        
    Returns:
        str: The formatted JSON string, or None if there is an error.
    """
    try:
        formatted_result = json.dumps(result, indent=4, default=str, ensure_ascii=False)
        return formatted_result
    except Exception as e:
        print(f"Error formatting result: {e}")
        return None

def get_all_cats(db: Database):
    """Fetches all cats from the database and prints their details.
    
    Args:
        db: The MongoDB database instance.
    """
    try:
        result = db.cats.find({})
        for record in result:
            formatted_result = format_result(record)
            if formatted_result:
                print(formatted_result)
    except Exception as e:
        print(f"Error retrieving all cats: {e}")

def get_cat_by_name(db: Database, name: str):
    """Fetches a cat by name from the database and prints its details.
    
    Args:
        db: The MongoDB database instance.
        name (str): The name of the cat to search for.
    """
    try:
        result = db.cats.find_one({"name": name})
        if result:
            formatted_result = format_result(result)
            if formatted_result:
                print(formatted_result)
        else:
            print(f"No cat found with the name {name}.")
    except Exception as e:
        print(f"Error retrieving cat by name: {e}")

def update_cat_age(db: Database, name: str, age: int):
    """Updates the age of a cat by its name and prints the updated details.
    
    Args:
        db: The MongoDB database instance.
        name (str): The name of the cat whose age is to be updated.
        age (int): The new age of the cat.
    """
    try:
        result = db.cats.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count > 0:
            updated_cat = db.cats.find_one({"name": name})
            formatted_result = format_result(updated_cat)
            if formatted_result:
                print(formatted_result)
        else:
            print(f"Failed to update age for cat named {name}.")
    except Exception as e:
        print(f"Error updating cat's age: {e}")

def add_feature_to_cat(db: Database, name: str, new_feature: str):
    """Adds a new feature to a cat by its name and prints the updated details.
    
    Args:
        db: The MongoDB database instance.
        name (str): The name of the cat to which the feature is to be added.
        new_feature (str): The new feature to be added to the cat's list of features.
    """
    try:
        result = db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count > 0:
            updated_cat = db.cats.find_one({"name": name})
            formatted_result = format_result(updated_cat)
            if formatted_result:
                print(formatted_result)
        else:
            print(f"Failed to add feature to cat named {name}.")
    except Exception as e:
        print(f"Error adding feature to cat: {e}")

def delete_cat_by_name(db: Database, name: str):
    """Deletes a cat by its name from the database.
    
    Args:
        db: The MongoDB database instance.
        name (str): The name of the cat to be deleted.
    """
    try:
        result = db.cats.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Record with name '{name}' was successfully deleted!")
        else:
            print(f"No cat found with the name {name} to delete.")
    except Exception as e:
        print(f"Error deleting cat by name: {e}")

def delete_all_cats(db: Database):
    """Deletes all cats from the collection.
    
    Args:
        db: The MongoDB database instance.
    """
    try:
        result = db.cats.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except Exception as e:
        print(f"Error deleting all cats: {e}")
