from utils import execute_query

def update_record(query: str, params: tuple, success_message: str, fail_message: str):
    """
    Executes an update query and displays a success or failure message.

    Args:
        query (str): The SQL update query to execute.
        params (tuple): Parameters to bind to the query.
        success_message (str): Message to display if the update is successful.
        fail_message (str): Message to display if the update fails.
    """
    result = execute_query(query, params)
    
    if result:
        print(success_message)
    else:
        print(fail_message)


def update_task_status(task_id: int, new_status: str):
    """
    Updates the status of a task based on the provided status name.

    Args:
        task_id (int): The ID of the task to update.
        new_status (str): The new status name to set.
    """
    query = """
        UPDATE tasks
        SET status_id = (
            SELECT id FROM status WHERE name = %s LIMIT 1
        )
        WHERE id = %s;
    """
    success_message = f"Task {task_id} status successfully updated to '{new_status}'."
    fail_message = f"Task {task_id} status update failed. Task may not exist."
    update_record(query, (new_status, task_id), success_message, fail_message)


def update_user_name(user_id: int, new_name: str):
    """
    Updates the full name of a user based on the provided user ID.

    Args:
        user_id (int): The ID of the user to update.
        new_name (str): The new name to set for the user.
    """
    query = """
        UPDATE users
        SET fullname = %s
        WHERE id = %s;
    """
    success_message = f"User {user_id} name successfully updated to '{new_name}'."
    fail_message = f"User {user_id} name update failed. User may not exist."
    update_record(query, (new_name, user_id), success_message, fail_message)
