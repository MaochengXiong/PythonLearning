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


def unpack(bytes):
    return json.loads(bytes)