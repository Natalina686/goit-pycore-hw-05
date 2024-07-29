import sys
import re
from collections import defaultdict

def parse_log_file(file_path):
    # парсимо логфайл та повертаємо словник з рівнями логування та записами
    log_entries = defaultdict(list)
    
    with open(file_path, 'r') as file:
        for line in file:
            # використовуємо регулярний вираз для знаходження рівня логування
            match = re.match(r'(\S+ \S+) - (\w+): (.*)', line)
            if match:
                timestamp, level, message = match.groups()
                log_entries[level].append((timestamp, message))
    
    return log_entries

def print_log_summary(log_entries):
    # виводимо статистику по рівнях логування
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    
    for level in sorted(log_entries.keys()):
        print(f"{level:<17} | {len(log_entries[level])}")

def print_log_details(log_entries, level):
    # виводимо деталі записів для вказаного рівня логування
    print(f"\nДеталі логів для рівня '{level}':")
    for timestamp, message in log_entries.get(level, []):
        print(f"{timestamp} - {message}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /path/to/logfile.log [level]")
        return
    
    file_path = sys.argv[1]
    level_filter = sys.argv[2].upper() if len(sys.argv) > 2 else None
    
    log_entries = parse_log_file(file_path)

    # підсумовуємо
    print_log_summary(log_entries)

    # якщо вказано рівень логування, виводимо деталі
    if level_filter and level_filter in log_entries:
        print_log_details(log_entries, level_filter)
    elif level_filter:
        print(f"Рівень '{level_filter}' не знайдено в логах.")

if __name__ == "__main__":
    main()