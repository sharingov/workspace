r, o, g = 0, 0, 0
for i in range(int(input()) * int(input())):
    s = input()
    if "роз" in s:
        r += 1
    elif "орхид" in s:
        o += 1
    elif "гиацинт" in s:
        g += 1

if g >= r:
    if g >= o:
        print("Гиацинты", end=" ")
        if o >= r:
            print("Орхидеи", end=" ")
            print("Розы")
        else:
            print("Розы", end=" ")
            print("Орхидеи")
    else:
        print("Орхидеи", end=" ")
        print("Гиацинты", end=" ")
        print("Розы")
else:
    if o >= r:
        print("Орхидеи", end=" ")
        print("Розы", end=" ")
        print("Гиацинты")
    else:
        print("Розы", end=" ")
        if g >= o:
            print("Гиацинты", end=" ")
            print("Орхидеи")
        else:
            print("Орхидеи", end=" ")
            print("Гиацинты")
