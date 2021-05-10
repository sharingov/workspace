import re

def minion_game(string):
    vowels = "AEIOU"
    kev = stu = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kev += len(string)-i
        else:
            stu += len(string)-i
    if kev == stu:
        print("Draw")
    elif kev > stu:
        print("Kevin", kev)
    else:
        print("Stuart", stu)

if __name__ == '__main__':
    s = input()
    minion_game(s)
