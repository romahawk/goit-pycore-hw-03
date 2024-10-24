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