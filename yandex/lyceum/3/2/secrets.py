def print_document(pages):
    for page in pages:
        if page.startswith("Секретно"):
            print("Дальнейшие материалы засекречены")
            return
        print(page)
    print("Напечатано без купюр")
