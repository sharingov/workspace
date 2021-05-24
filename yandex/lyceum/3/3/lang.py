def translate(next):
    global translated_text
    translated_text = " ".join(
        " ".join(
            [
                "".join(
                    [r for r in s if r.lower() in "бвгджзйклмнпрстфхцчшщьъ"]
                )
                for s in next.split()
            ]
        ).split()
    )
