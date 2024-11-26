import psycopg2
from faker import Faker
from random import choice
from constants import DB_CONFIG, NUM_USERS, NUM_STATUSES, NUM_TASKS

def populate_tables():
    """
    Populates the database tables with initial fake data using the Faker library.
    Fills the `status`, `users`, and `tasks` tables.
    """
    fake = Faker()

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                populate_status_table(cur)
                populate_users_table(cur, fake, NUM_USERS)
                populate_tasks_table(cur, fake, NUM_TASKS)

            conn.commit()
            print("All tables populated successfully!")
    except Exception as e:
        print(f"Error during data population: {e}")

def populate_status_table(cur):
    """
    Populates the `status` table with predefined status names.

    Args:
        cur: Database cursor for executing queries.
    """
    status_names = ["new", "in progress", "completed", "on hold", "cancelled"]
    for name in status_names:
        cur.execute(
            "INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;",
            (name,)
        )

    print("Status table populated successfully!")

def populate_users_table(cur, fake, num_users):
    """
    Populates the `users` table with fake user data.

    Args:
        cur: Database cursor for executing queries.
        fake: Faker instance for generating fake data.
        num_users: Number of users to generate.
    """
    for _ in range(num_users):
        fullname = fake.name()
        email = fake.unique.email()
        cur.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s);",
            (fullname, email)
        )

    print(f"Users table populated with {num_users} records!")

def populate_tasks_table(cur, fake, num_tasks):
    """
    Populates the `tasks` table with fake task data.

    Args:
        cur: Database cursor for executing queries.
        fake: Faker instance for generating fake data.
        num_tasks: Number of tasks to generate.
    """
    cur.execute("SELECT id FROM users;")
    user_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT id FROM status;")
    status_ids = [row[0] for row in cur.fetchall()]

    for _ in range(num_tasks):
        title = fake.sentence(nb_words=5)
        description = fake.text(max_nb_chars=200)
        status_id = choice(status_ids)
        user_id = choice(user_ids)
        cur.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
            (title, description, status_id, user_id)
        )

    print(f"Tasks table populated with {num_tasks} records!")