# Аналіз числового списку
def get_min_max(numbers):
    # Беремо перший елемент за початковий орієнтир
    min_val = numbers[0]
    max_val = numbers[0]
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return (min_val, max_val) # Повертаємо кортеж

def get_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def get_average(numbers):
    total = get_sum(numbers)
    # Рахуємо кількість елементів без len()
    count = 0
    for _ in numbers:
        count += 1
    return total / count

# Робота з вкладеними списками

def flatten_list(nested_list):
    flat_list = []
    # Подвійний цикл: спочатку по списках, потім по їх елементах
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def sort_ascending(numbers):
    # Використовуємо просте "сортування бульбашкою", 
    # щоб повністю уникнути вбудованого методу .sort()
    count = 0
    for _ in numbers:
        count += 1
        
    for i in range(count):
        for j in range(0, count - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Міняємо місцями, якщо попередній більший за наступний
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Статистика оцінок студентів

def get_top_student(students):
    top_student = students[0]
    for student in students:
        # student[1] - це оцінка (другий елемент кортежу)
        if student[1] > top_student[1]:
            top_student = student
    return top_student

def get_grades_only(students):
    grades = []
    for student in students:
        grades.append(student[1])
    return grades

def count_students_above(students, threshold):
    count = 0
    for student in students:
        if student[1] > threshold:
            count += 1
    return count

# Основна частина (тестування)

def main():
    print("--- ЗАВДАННЯ 1 ---")
    num_list = [15, 42, 8, 100, 4, 23, 16, 88, 55, 30] # 10 елементів
    print(f"Початковий список: {num_list}")
    
    min_max_tuple = get_min_max(num_list)
    print(f"Кортеж (мінімум, максимум): {min_max_tuple}")
    print(f"Сума елементів: {get_sum(num_list)}")
    print(f"Середнє арифметичне: {get_average(num_list)}")


    print("\n--- ЗАВДАННЯ 2 ---")
    data = [[1, 4, 7], [2, 5], [9, 3, 6, 8]]
    print(f"Вкладений список: {data}")
    
    flat_data = flatten_list(data)
    print(f"Одновимірний список: {flat_data}")
    
    sorted_data = sort_ascending(flat_data)
    print(f"Відсортований список: {sorted_data}")


    print("\n--- ЗАВДАННЯ 3 ---")
    students = [
        ("Іван", 85),
        ("Марія", 92),
        ("Олег", 78),
        ("Анна", 90)
    ]
    
    top_stud = get_top_student(students)
    print(f"Студент з найвищою оцінкою: {top_stud}")
    
    grades_list = get_grades_only(students)
    print(f"Список лише з оцінок: {grades_list}")
    
    threshold = 85
    above_count = count_students_above(students, threshold)
    print(f"Кількість студентів з оцінкою вище {threshold}: {above_count}")

if __name__ == "__main__":
    main()