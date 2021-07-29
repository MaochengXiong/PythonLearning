import json


def json2Bytes(json):
    return bytes(json.encode())


def __pack__(code, data):
    return json.dumps({'code': code, 'data': data})


def pack_text(data):
    return __pack__(0, data)


def pack_cards_of_self(data):
    return __pack__(1, data)


def pack_play_cards(data):
    return __pack__(2, data)


def pack_your_turn():
    return __pack__(3, 'Your turn')


def pack_play_legal():
    return __pack__(4, 'play success')


def pack_play_illegal():
    return __pack__(5, 'illegal cards')

def unpack(bytes):
    return json.loads(bytes)