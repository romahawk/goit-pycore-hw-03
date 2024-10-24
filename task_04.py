# define congrats 7 days ahead

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дату народження в об'єкт datetime.date
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        # Створюємо дату народження на цей рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, беремо дату наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження відбувається протягом наступних 7 днів
        if 0 <= (birthday_this_year - today).days <= 7:
            # Якщо день народження випадає на вихідний, переносимо на наступний понеділок
            if birthday_this_year.weekday() > 4:  # 5 і 6 - це субота і неділя
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            # Додаємо користувача до списку з датою привітання
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.10.30"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Peter Parker", "birthday": "1993.01.30"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's list of congrats:", upcoming_birthdays)