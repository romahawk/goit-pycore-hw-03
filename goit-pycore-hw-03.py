# write  a function caclculating difference between dates

from datetime import datetime, timedelta

def days_between_two_dates(date_one: str, date_two: str) -> int:

  first_date = datetime.strptime(date_one, "%Y-%m-%d")
  second_date = datetime.strptime(date_two, "%Y-%m-%d")
  print(first_date)

  return first_date - second_date

print(days_between_two_dates("2024-10-23", "2024-10-1"))



# -----------------------------------------------------------------------------------
# write a unique random numbers function 

import random

def get_numbers_ticket(min, max, quantity):
  # check input parameters are correct
  if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity <= 0:
    return[]
  
  # generate unique random numbers
  lottery_numbers = random.sample(range(min, max +1), quantity)

  # return sorted list
  return sorted(lottery_numbers)

# use case
lottery_numbers = get_numbers_ticket(1, 100, 7)
print("Your lottery numbers:", lottery_numbers)


# ------------------------------------------------------------------------------
import re 

def normalize_phone(phone_number):
  # delete all symbols except numbers and plus
  clean_number = re.sub(r'[^\d+]', '', phone_number.strip())

  # if number begins from '380' we add only '+' 
  if clean_number.startswith('380'):
    clean_number = '+' + clean_number
  # if number does not begin from '+' we add code '+38'
  elif not clean_number.startswith('+'):
    clean_number = '+38' + clean_number

  return clean_number

# example
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# ------------------------------------------------------------------------------
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
print("Список привітань на цьому тижні:", upcoming_birthdays)
