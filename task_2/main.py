from db_operations import (
    get_db_connection,
    get_all_cats,
    get_cat_by_name,
    update_cat_age,
    add_feature_to_cat,
    delete_cat_by_name,
    delete_all_cats
)
from utils import input_cat_name, input_cat_age, input_new_feature

def main():
    # Connect to the database
    db = get_db_connection()
    if db is None:
        return

    # Example operations
    print("\nRetrieving all cats:")
    get_all_cats(db)

    print("\nSearching for a cat by name:")
    get_cat_by_name(db, input_cat_name())

    print("\nUpdating a cat's age:")
    update_cat_age(db, input_cat_name(), input_cat_age())

    print("\nAdding a feature to a cat:")
    add_feature_to_cat(db, input_cat_name(), input_new_feature())

    print("\nDeleting a cat by name:")
    delete_cat_by_name(db, input_cat_name())

    print("\nDeleting all cats:")
    delete_all_cats(db)

if __name__ == "__main__":
    main()
