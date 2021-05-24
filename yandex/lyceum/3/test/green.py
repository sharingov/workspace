def green_remove(s: str):
    print(' '.join(list(e for e in s.split() if 'зелён' not in e.lower())))
