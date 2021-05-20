def task(s):
    le = len(s)
    if le < 4 or le > 11:
        return False
    if "прям" in s:
        return False
    if "крю" in s:
        if le % 2 == 1:
            return False
    elif "кря" in s:
        if le % 2 == 0:
            return False
    if s > "скрюченный":
        return False
    return True


s = input()
print("Скрючено" if task(s) else "Не скрючено")
