
from datetime import date
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
birth_date = input("Enter birth date (DD/MM/YYYY): ")
day, month, year = map(int, birth_date.split('/'))
age = calculate_age(date(year, month, day))
print("You are", age, "years old.")