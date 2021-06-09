import sys

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

for line in sys.stdin.readlines():
    p = morph.parse(line.rstrip())[0]
    if "NOUN" in p.tag:
        ans = morph.parse("живой")[0].inflect(
            {p.tag.number, p.tag.gender, "nomn"}
        )
        ans = ans.word if ans else "живые"
        if "inan" in p.tag:
            ans = "не " + ans
        print(ans.capitalize())
    else:
        print("Не существительное")
