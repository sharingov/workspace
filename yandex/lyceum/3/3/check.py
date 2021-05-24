cart = []
things = 0
total = 0
number = 1


def add_item(s, n):
    global things, total
    cart.append((s, n))
    things += 1
    total += n


def print_receipt():
    if cart:
        global number, things, total
        print(
            f"Чек {number}. Всего предметов: {things}",
            *map(lambda x: x[0] + " - " + str(x[1]), cart),
            f"Итого: {total}",
            "-----",
            sep="\n",
        )
        del cart[:]
        things = 0
        total = 0
        number += 1
