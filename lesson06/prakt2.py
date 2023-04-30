#Написати функцію, яка буде підносити число у квадрат. 
#Написати другу, яка буде перевіряти, чи є число простим.
#Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map
def square(a):
    return a**2


def issimple(N):
    res = True
    for i in range(2,N):
        if not N % i:
            res = False
            break
    return res


lst = list(range(51))
print(list(map(square, filter(issimple, lst))))

