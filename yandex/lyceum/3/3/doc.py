def hello(s):
    print(f"Здравствуйте, {s}! Вашу карту ищут...")


def search_card(s):
    global base
    try:
        i = base.index(s) + 1
    except ValueError:
        print("Ваша карта не найдена")
    else:
        print(f"Ваша карта с номером {i} найдена")
