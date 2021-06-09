class Person:
    def __init__(self, name, father, surname, numbers):
        self.name = name
        self.father = father
        self.surname = surname
        self.numbers = numbers

    def get_phone(self):
        return self.numbers.get("private")

    def get_work_phone(self):
        return self.numbers.get("work")

    def get_name(self):
        return " ".join((self.surname, self.name, self.father))

    def get_sms_text(self):
        return (
            f"Уважаемый {self.name} {self.father}! Примите участие в нашем "
            "беспроигрышном конкурсе для физических лиц"
        )


class Company:
    def __init__(self, name, _type, numbers, *employees):
        self.name = name
        self._type = _type
        self.numbers = numbers
        self.employees = list(employees)

    def get_phone(self):
        return self.numbers.get(
            "contact",
            next(
                (
                    e.get_work_phone()
                    for e in self.employees
                    if e.get_work_phone()
                ),
                None,
            ),
        )

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return (
            f"Для компании {self.name} есть супер предложение! "
            f"Примите участие в нашем беспроигрышном конкурсе для {self._type}"
        )


def send_sms(*args):
    for arg in args:
        if arg.get_phone():
            print(
                f"Отправлено СМС на номер {arg.get_phone()} "
                f"с текстом: {arg.get_sms_text()}"
            )
        else:
            print(f"Не удалось отправить сообщение абоненту: {arg.get_name()}")
