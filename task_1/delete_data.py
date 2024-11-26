from utils import execute_query

def delete_task(task_id: int):
    """
    Deletes a task from the database based on the given task ID.

    Args:
        task_id (int): The ID of the task to be deleted.
    """
    query = "DELETE FROM tasks WHERE id = %s;"
    success_message = f"Task with ID {task_id} successfully deleted."
    fail_message = f"Failed to delete task with ID {task_id}. Task may not exist."

    result = execute_query(query, (task_id,))

    if result:
        print(success_message)
    else:
        print(fail_message)