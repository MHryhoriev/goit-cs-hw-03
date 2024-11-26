from utils import execute_query, display_results

def get_tasks_by_user(user_id: int):
    """
    Retrieve all tasks assigned to a specific user.

    Args:
        user_id (int): The ID of the user.
    """
    query = "SELECT * FROM tasks WHERE user_id = %s;"
    rows = execute_query(query, (user_id,))
    display_results(rows)

def get_tasks_by_status(status: str):
    """
    Retrieve all tasks with a specific status.

    Args:
        status (str): The name of the status.
    """
    query = """
        SELECT * 
        FROM tasks 
        WHERE status_id = (SELECT id FROM status WHERE name = %s);
    """
    rows = execute_query(query, (status,))
    display_results(rows)

def get_users_without_tasks():
    """
    Retrieve all users who do not have any assigned tasks.
    """
    query = """
        SELECT *
        FROM users
        WHERE id NOT IN (SELECT user_id FROM tasks WHERE user_id IS NOT NULL);
    """
    rows = execute_query(query)
    display_results(rows)

def get_incomplete_tasks():
    """
    Retrieve all tasks that are not marked as 'completed'.
    """
    query = """
        SELECT *
        FROM tasks
        WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
    """
    rows = execute_query(query)
    display_results(rows)

def find_users_by_email(email: str):
    """
    Retrieve users whose email matches a specific pattern.

    Args:
        email (str): The email pattern to search for (supports SQL LIKE syntax).
    """
    query = "SELECT * FROM users WHERE email LIKE %s;"
    rows = execute_query(query, (email,))
    display_results(rows)

def get_tasks_by_email_domain(domain: str):
    """
    Retrieve tasks assigned to users with a specific email domain.

    Args:
        domain (str): The email domain to filter by (e.g., '%@example.com').
    """
    query = """
        SELECT *
        FROM tasks
        JOIN users ON users.id = tasks.user_id
        WHERE users.email LIKE %s;
    """
    rows = execute_query(query, (domain,))
    display_results(rows)

def get_tasks_without_description():
    """
    Retrieve all tasks that do not have a description or have an empty description.
    """
    query = """
        SELECT *
        FROM tasks
        WHERE description IS NULL OR description = '';
    """
    rows = execute_query(query)
    display_results(rows)

def get_users_with_task_count():
    """
    Retrieve all users along with the count of tasks assigned to each.
    """
    query = """
        SELECT users.fullname, COUNT(tasks.id) AS task_count
        FROM users
        LEFT JOIN tasks ON users.id = tasks.user_id
        GROUP BY users.fullname;
    """
    rows = execute_query(query)
    display_results(rows)