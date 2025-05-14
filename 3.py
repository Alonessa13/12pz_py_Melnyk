    import random

    # Створення великого списку з повтореннями
    numbers = [random.randint(1, 100) for _ in range(1000)]

    # Підрахунок кількості повторень
    counter = {}
    for num in numbers:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    # Пошук числа з найбільшою кількістю повторів
    max_number = None
    max_count = 0

    for num, count in counter.items():
        if count > max_count:
            max_count = count
            max_number = num

    print(f"Найчастіше зустрічається число {max_number} — {max_count} разів.")
