# write  a function caclculating difference between dates

from datetime import datetime, timedelta

def days_between_two_dates(date_one: str, date_two: str) -> int:

  first_date = datetime.strptime(date_one, "%Y-%m-%d")
  second_date = datetime.strptime(date_two, "%Y-%m-%d")
  print(first_date)

  return first_date - second_date

print(days_between_two_dates("2024-10-23", "2024-10-1"))