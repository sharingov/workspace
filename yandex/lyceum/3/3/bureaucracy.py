def setup_profile(a, b):
    global name, dates
    name, dates = a, b


def print_application_for_leave():
    global name, dates
    print(f"Заявление на отпуск в период {dates}. {name}")


def print_holiday_money_claim(amount):
    global name
    print(f"Прошу выплатить {amount} отпускных денег. {name}")


def print_attorney_letter(s):
    global name, dates
    print(
        f"На время отпуска в период {dates} "
        f"моим заместителем назначается {s}. {name}"
    )
