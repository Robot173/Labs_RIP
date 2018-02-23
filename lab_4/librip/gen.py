from random import randint

# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0, 'No args'
    if len(args) == 1:
        for i in items:
            if i[args[0]]:
                yield i[args[0]]
    else:
        for i in items:
            out = {}
            for q in args:
                if q in i:
                    if i[q]:
                        out[q] = i[q]
                else:
                    pass
            if out:
                yield out

    # Необходимо реализовать генератор
# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield randint(begin, end)
    # Необходимо реализовать генератор
