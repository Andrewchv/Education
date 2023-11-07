from datetime import date, timedelta

def get_birthdays_per_week(users):
    if not users:
        return {}

    # Знайти поточну дату та поточний тиждень
    today = date.today()
    current_day_of_week = today.weekday()
    last_day_of_current_week = today + timedelta(days=7)

    # Розділити користувачів за днями тижня, включаючи тих, чиї дні народження вже минули у цьому році
    new_users = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year)
        if birthday < today:  # якщо найближчий день народження менше поточної дати...
            birthday = birthday.replace(year=today.year + 1)
        # Перевірити, чи день народження випадає на поточний тиждень, включаючи тих, чиї дні народження вже минули у цьому році
        if today <= birthday <= last_day_of_current_week:
            # Якщо день народження припадає на вихідний (суботу або неділю), переносимо його на наступний понеділок

            weekday = birthday.weekday()
            if weekday == 0:
                new_users['Monday'].append(name)
            elif weekday == 1:
                new_users['Tuesday'].append(name)
            elif weekday == 2:
                new_users['Wednesday'].append(name)
            elif weekday == 3:
                new_users['Thursday'].append(name)
            elif weekday == 4:
                new_users['Friday'].append(name)
            elif weekday in (5, 6):
                new_users['Monday'].append(name)


    # Видаляємо порожні списки зі словника
    new_users = {day: names for day, names in new_users.items() if names}
    print(new_users)
    return new_users

if __name__ == "__main__":
	# Тестові дані з користувачами
	users = [
		{'name': 'Masha', 'birthday': date ( 2021, 11, 11 )},
		{'name': 'Olya', 'birthday': date ( 2023, 11, 12 )},
		{'name': 'Kolya', 'birthday': date ( 1993, 11, 10 )},
		# Додайте інших користувачів за потреби
	]

	result = get_birthdays_per_week ( users )
	print ( result )

	# Виводимо результат
	for day_name, names in result.items ( ):
		print ( f"{day_name}: {', '.join ( names )}" )