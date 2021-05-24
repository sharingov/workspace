horses = [False] * 10


def do_bet(n, m):
    global horses
    if n <= 0 or n > 10 or horses[n - 1] or m <= 0:
        print("Что-то пошло не так, попробуйте еще раз")
        return
    horses[n - 1] = True
    print(f"Ваша ставка в размере {m} на лошадь {n} принята")
