def func(dct, key, default):
    try:
        return dct[key]
    except KeyError:
        return default


if __name__ == '__main__':
    dct = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
    }
    print(func(dct, 7, 'e'))
