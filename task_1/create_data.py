from utils import execute_query
from typing import Optional

def add_task_to_user(user_id: int, title: str, description: Optional[str] = None, status_name: str = "new"):
    """
    Adds a new task to a specific user in the database.

    Args:
        user_id (int): The ID of the user to whom the task is assigned.
        title (str): The title of the task.
        description (Optional[str]): The description of the task. Defaults to None.
        status_name (str): The name of the task's status. Defaults to "new".
    """
    query = """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (
            %s,
            %s,
            (SELECT id FROM status WHERE name = %s LIMIT 1),
            %s
        );
    """
    success_message = f"New task '{title}' successfully added for user with ID {user_id}."
    fail_message = f"Failed to add new task for user with ID {user_id}. Check if the status '{status_name}' exists."

    result = execute_query(query, (title, description, status_name, user_id))
    
    if result:
        print(success_message)
    else:
        print(fail_message)