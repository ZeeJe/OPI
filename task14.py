from abc import ABC, abstractmethod

# Архітектурний шаблон MVC

# --- MODEL ---
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_all_orders(self):
        return self.orders

    def get_total_sum(self):
        total = 0
        for order in self.orders:
            total += order.amount
        return total

# --- VIEW ---
class OrderView:
    def show_menu(self):
        print("\n--- СИСТЕМА ЗАМОВЛЕНЬ (MVC) ---")
        print("1 - Додати замовлення")
        print("2 - Переглянути список замовлень")
        print("3 - Переглянути загальну суму")
        print("0 - Вихід з MVC та перехід до патернів")
        return input("Оберіть дію: ")

    def get_order_data(self):
        order_id = input("Введіть ID замовлення: ")
        try:
            amount = float(input("Введіть суму: "))
            return order_id, amount
        except ValueError:
            return None, None

    def display_orders(self, orders):
        if not orders:
            print("Список замовлень порожній.")
        else:
            print("\nСписок замовлень:")
            for order in orders:
                print(f"ID: {order.order_id} | Сума: {order.amount}")

    def display_total(self, total):
        print(f"\nЗагальна сума всіх замовлень: {total}")

    def display_message(self, message):
        print(message)

# --- CONTROLLER ---
class OrderController:
    def __init__(self, model_repository, view):
        self.model = model_repository
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            
            if choice == '1':
                o_id, amt = self.view.get_order_data()
                if o_id and amt is not None:
                    new_order = Order(o_id, amt)
                    self.model.add_order(new_order)
                    self.view.display_message("Замовлення успішно додано!")
                else:
                    self.view.display_message("Помилка вводу даних.")
            
            elif choice == '2':
                orders = self.model.get_all_orders()
                self.view.display_orders(orders)
                
            elif choice == '3':
                total = self.model.get_total_sum()
                self.view.display_total(total)
                
            elif choice == '0':
                self.view.display_message("Завершення роботи MVC...\n")
                break
            else:
                self.view.display_message("Невідома команда.")

# Патерн Strategy (Стратегія)

# 1. Абстрактна стратегія
class IPriceStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price):
        pass

# 2. Конкретні стратегії
class NoDiscountStrategy(IPriceStrategy):
    def calculate(self, base_price):
        return base_price

class LoyalCustomerStrategy(IPriceStrategy):
    def calculate(self, base_price):
        return base_price * 0.90  # 10% знижки

class LargeOrderStrategy(IPriceStrategy):
    def calculate(self, base_price):
        return base_price * 0.80  # 20% знижки

# 3. Клас, що використовує стратегію
class PriceCalculator:
    def __init__(self, strategy: IPriceStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: IPriceStrategy):
        self.strategy = strategy

    def get_final_price(self, base_price):
        return self.strategy.calculate(base_price)

def test_strategy():
    print("--- ТЕСТ ПАТЕРНУ STRATEGY ---")
    base_price = 1000
    calculator = PriceCalculator(NoDiscountStrategy())
    print(f"Без знижки: {calculator.get_final_price(base_price)}")

    calculator.set_strategy(LoyalCustomerStrategy())
    print(f"Постійний клієнт (10%): {calculator.get_final_price(base_price)}")

    calculator.set_strategy(LargeOrderStrategy())
    print(f"Велике замовлення (20%): {calculator.get_final_price(base_price)}\n")

# Патерн Observer (Спостерігач)

# Абстрактний спостерігач
class IObserver(ABC):
    @abstractmethod
    def update(self, order_id):
        pass

# Конкретні спостерігачі
class LoggerObserver(IObserver):
    def update(self, order_id):
        print(f"Лог: Створено нове замовлення з ID {order_id}")

class NotificationObserver(IObserver):
    def update(self, order_id):
        print(f"Сповіщення: Відправлено email клієнту про замовлення {order_id}")

# Суб'єкт (той, за ким спостерігають)
class OrderService:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer: IObserver):
        self.subscribers.append(observer)

    def notify_all(self, order_id):
        for observer in self.subscribers:
            observer.update(order_id)

    def create_order(self, order_id):
        print(f"Система: Замовлення {order_id} збережено в базу.")
        self.notify_all(order_id)

def test_observer():
    print("--- ТЕСТ ПАТЕРНУ OBSERVER ---")
    service = OrderService()
    
    logger = LoggerObserver()
    notifier = NotificationObserver()
    
    service.subscribe(logger)
    service.subscribe(notifier)
    
    service.create_order("ORD-777")

# ТОЧКА ВХОДУ

if __name__ == "__main__":
    # Запуск MVC (Завдання 1)
    repo = OrderRepository()
    view = OrderView()
    controller = OrderController(repo, view)
    controller.run()
    
    # Запуск тестів патернів (Завдання 2 та 3)
    test_strategy()
    test_observer()