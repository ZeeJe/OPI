from collections import deque

# Стек (stack, LIFO)

print("--- ЧАСТИНА 1: СТЕК ---")

# 1. Реалізація стеку
stack = []
print("Створено порожній стек:", stack)

# Додаємо 5 елементів
for i in range(1, 6):
    stack.append(i)
print("Стек після додавання 5 елементів:", stack)

# Видаляємо 2 елементи
stack.pop()
stack.pop()
print("Стек після видалення 2 елементів:", stack)

# 2. Перевірка порожності
def is_empty(s):
    return len(s) == 0

# 3. Верхній елемент
def peek(s):
    if not is_empty(s):
        return s[-1]
    return "Стек порожній"

print(f"Чи порожній стек? {is_empty(stack)}")
print(f"Верхній елемент стеку: {peek(stack)}")

# 4. Реверс рядка за допомогою стеку
user_string = input("\nВведіть рядок для реверсу: ")
char_stack = []
for char in user_string:
    char_stack.append(char)

reversed_string = ""
while not is_empty(char_stack):
    reversed_string += char_stack.pop()

print(f"Обернений рядок: {reversed_string}")

# Черга (queue, FIFO)

print("\n--- ЧАСТИНА 2: ЧЕРГА ---")

# 1. Реалізація черги
queue = deque()
print("Додаємо елементи в чергу:")
for i in range(1, 6):
    queue.append(f"Клієнт {i}")
    print(f"  Додано: Клієнт {i}. Черга: {list(queue)}")

print("\nВидаляємо елементи з черги:")
for _ in range(3):
    removed = queue.popleft()
    print(f"  Видалено: {removed}. Черга: {list(queue)}")

# 2. Симуляція черги в магазині
print("\nСимуляція черги в магазині:")
store_queue = deque()

def add_to_store(name):
    store_queue.append(name)
    print(f"[+] {name} став(ла) у чергу.")

def serve_store():
    if store_queue:
        client = store_queue.popleft()
        print(f"[-] Обслуговано клієнта: {client}")
    else:
        print("[-] Черга порожня, нікого обслуговувати.")

def view_store_queue():
    print(f"[*] Поточна черга: {list(store_queue)}")

add_to_store("Олексій")
add_to_store("Марина")
view_store_queue()
serve_store()
view_store_queue()

# Словники (dictionary)

print("\n--- ЧАСТИНА 3: СЛОВНИКИ ---")

# 1. Базовий словник
# Згідно із завданням, вік та група - це кортеж (age, group)
student = {
    "ім'я": "Іван",
    "вік_та_група": (19, "КН-21") 
}
print(f"Початковий словник: {student}")

student["середній_бал"] = 4.5
print(f"Після додавання нової пари: {student}")

student["ім'я"] = "Іван Петренко"
print(f"Після оновлення значення: {student}")

del student["вік_та_група"]
print(f"Після видалення елемента: {student}")

# 2. Оновлення даних (підрахунок оцінок)
print("\nПідрахунок оцінок:")
marks = [5, 4, 5, 3, 4, 5, 3]
marks_count = {}

for mark in marks:
    if mark in marks_count:
        marks_count[mark] += 1
    else:
        marks_count[mark] = 1

print(f"Список оцінок: {marks}")
print(f"Словник (оцінка: кількість): {marks_count}")

# 3. Реалізація меню
print("\n--- ІНТЕРАКТИВНЕ МЕНЮ ТОВАРІВ ---")
products = {}

while True:
    print("\nМеню:")
    print("1 — додати товар")
    print("2 — видалити товар")
    print("3 — показати всі товари")
    print("0 — вихід")
    
    choice = input("Оберіть дію (введіть цифру): ")
    
    if choice == '1':
        name = input("Введіть назву товару: ")
        price = input("Введіть ціну товару: ")
        products[name] = price
        print(f"Товар '{name}' успішно додано!")
        
    elif choice == '2':
        name = input("Введіть назву товару для видалення: ")
        if name in products:
            del products[name]
            print(f"Товар '{name}' видалено!")
        else:
            print("Такого товару немає в базі.")
            
    elif choice == '3':
        if not products:
            print("Список товарів порожній.")
        else:
            print("Список товарів:")
            for n, p in products.items():
                print(f"- {n}: {p} грн")
                
    elif choice == '0':
        print("Вихід з програми. Роботу завершено!")
        break # Вихід з безкінечного циклу
        
    else:
        print("Невідома команда, спробуйте ще раз.")