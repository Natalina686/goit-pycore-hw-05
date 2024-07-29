import re
from typing import Callable

def generator_numbers(text: str):
    # регулярний вираз для знаходження дійсних чисел
    pattern = r'\b\d+\.\d{2}\b'
    # знаходимо всі дійсні числа в тексті
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)
    # повертаємо числа float
def sum_profit(text: str, func: Callable) -> float:
    # використовуємо генератор щоб підсумувати числа
    return sum(func(text))

# приклад
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_incom = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_incom}")