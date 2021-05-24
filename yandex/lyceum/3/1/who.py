def who_are_you_and_hello():
    s = input()
    while not (s.isalpha() and s == s.capitalize() and len(s.split()) == 1):
        s = input()
    print(f'Привет, {s}!')
