def parse(query: str) -> dict:
    dict = {}
    try:
        src = query.split('?')[1]
    except IndexError:
        return dict

    for item in src.split('&'):
        pair = item.split('=')
        try:
            dict[pair[0]] = pair[1]
        except IndexError:
            pass

    return dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    src = query.split(';')
    dict = {}
    try:
        for item in src:
            pair = item.split('=', 1)
            dict[pair[0]] = pair[1]
    except IndexError:
        pass

    return dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
