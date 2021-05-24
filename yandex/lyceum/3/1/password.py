def ask_password():
    password = 'password'
    for i in range(3):
        if input() == password:
            print('Пароль принят')
            return
    print('В доступе отказано')
