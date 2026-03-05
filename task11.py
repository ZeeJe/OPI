def sum_of_set(numbers_set):
    """Функція приймає множину та повертає суму її елементів."""
    total = 0
    # Здійснюємо прохід по множині, додаючи кожен елемент до загальної суми
    for num in numbers_set:
        total += num
    return total

def check_number_in_set(numbers_set, target_number):
    """Функція за допомогою циклу перевіряє, чи належить число до множини."""
    is_found = False
    for num in numbers_set:
        if num == target_number:
            is_found = True
            break  # Якщо число знайдено, зупиняємо цикл
    
    if is_found:
        print(f"Число {target_number} належить до сформованої множини.")
    else:
        print(f"Число {target_number} не знайдено у множині.")

def main():
    # 1. Введення послідовності чисел та формування множини
    user_input = input("Введіть послідовність цілих чисел через пробіл: ")
    
    try:
        # Перетворюємо рядок на список цілих чисел, а потім — на множину (що залишить лише унікальні)
        numbers_list = [int(x) for x in user_input.split()]
        unique_set = set(numbers_list)
        print(f"\nСформована множина унікальних значень: {unique_set}")
        
        # 2. Обробка елементів: кількість чисел, більших за задане
        threshold = int(input("\nВведіть число для порівняння (щоб знайти більші за нього): "))
        count_greater = 0
        for num in unique_set:
            if num > threshold:
                count_greater += 1
        print(f"Кількість елементів множини, що більші за {threshold}: {count_greater}")
        
        # 3. Виклик функції для підрахунку суми
        total_sum = sum_of_set(unique_set)
        print(f"\nСума всіх елементів множини: {total_sum}")
        
        # 4. Перевірка належності числа до множини через власну функцію з циклом
        search_num = int(input("\nВведіть число для перевірки його наявності у множині: "))
        check_number_in_set(unique_set, search_num)
        
    except ValueError:
        print("\nПомилка: будь ласка, переконайтеся, що ви вводите лише цілі числа.")

# Точка входу в програму
if __name__ == "__main__":
    main()