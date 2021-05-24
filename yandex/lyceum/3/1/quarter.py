def quarter(x, y):
    d = {
        -3: 'III четверть',
        -1: 'II четверть',
        1: 'IV четверть',
        3: 'I четверть',
    }
    print(d[2 * (x / abs(x)) + (y / abs(y))])
