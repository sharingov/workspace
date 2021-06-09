import re


def ask_password(login, password, success, failure):
    login, password = login.lower(), password.lower()
    err = (
        int(len(re.findall("[aeuioy]", password)) != 3)
        + int(
            "".join(x for x in login if x.isalpha() and x not in "aueioy")
            != "".join(x for x in password if x not in "aueioy")
        )
        * 2
    )
    calls = [
        "",
        "Wrong number of vowels",
        "Wrong consonants",
        "Everything is wrong",
    ]

    return failure(login, calls[err]) if err else success(login)


def main(login, password):
    ask_password(
        login,
        password,
        lambda login: print(f"Привет, {login}!"),
        lambda login, err: print(
            f"Кто-то пытался притвориться пользователем {login}, "
            f"но в пароле допустил ошибку: {err.upper()}."
        ),
    )
