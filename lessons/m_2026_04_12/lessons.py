# f(x) = y - Функция в математике

# f(входные параметры) -> значение возвращаемое функцией

# аналог f(x^2) = y
def fun(number):
    return number ** 2

def is_adult(age):
    if age < 18:
        print(f"НЕ взрослый ({age})")
    else:
        print(f"взрослый ({age})")


for age in range(16, 22):
    is_adult(age)
