# Словник студентів і їхніх оцінок
grades = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

# Запит користувача
name = input("Введіть ім'я студента: ").strip()

# Пошук з обробкою помилки
if name in grades:
    print(f"Оцінка студента {name}: {grades[name]}")
else:
    print("Студента з таким ім'ям не знайдено.")
