#Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру. Друга функція прийматиме рядок та приводитиме його до верхнього регістру.
#Головна програма має застосовувати обидві функції до списку рядків за допомогою map, для кожного з рядків, та друкувати результат.
def tolower(s):
    return s.lower()


def toupper(s):
    return s.upper()


strings = ['Hello to EVERYBODY!', 'Welcome to HELL!', 'yOu\'Ll NeVeR wAlK aLoNe']
print(list(map(tolower, strings)))
print(list(map(toupper, strings)))
