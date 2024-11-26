from create_db_tables import create_db_tables
from seed import populate_tables
from get_data import (
    get_tasks_by_user, 
    get_tasks_by_status, 
    get_users_without_tasks, 
    get_incomplete_tasks, 
    find_users_by_email, 
    get_tasks_by_email_domain, 
    get_tasks_without_description,
    get_users_with_task_count
)
from update_data import update_task_status, update_user_name
from create_data import add_task_to_user
from delete_data import delete_task

def main():
    create_db_tables()
    populate_tables()

    # Отримати всі завдання певного користувача
    get_tasks_by_user(2)
    
    # Вибрати завдання за певним статусом
    get_tasks_by_status('new')

    # Отримати список користувачів, які не мають жодного завдання
    get_users_without_tasks()

    # Отримати всі завдання, які ще не завершено
    get_incomplete_tasks()

    # Знайти користувачів з певною електронною поштою
    find_users_by_email('scott%')

    # Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
    get_tasks_by_email_domain('%@example.net')

    # Отримати список завдань, що не мають опису
    get_tasks_without_description()

    # Отримати користувачів та кількість їхніх завдань
    get_users_with_task_count()

    # Оновити статус конкретного завдання
    update_task_status(1, 'In progress')

    # Оновити ім'я користувача
    update_user_name(3, 'Mike')

    # Додати нове завдання для конкретного користувача.
    add_task_to_user(
        title="Finish report",
        description="Complete the financial report for Q3",
        status_name="in progress",
        user_id=3
    )

    # Видалити конкретне завдання.
    delete_task(3)


if __name__ == "__main__":
    main()