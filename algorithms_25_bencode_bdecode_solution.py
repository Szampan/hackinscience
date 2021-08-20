def bencode(obj):
    if isinstance(obj, str):
        return f"{len(obj)}:{obj}".encode(encoding="utf-8")
    if isinstance(obj, int):
        return f"i{obj}e".encode(encoding="utf-8")
    if isinstance(obj, list):
        return b"l" + b"".join(bencode(item) for item in obj) + b"e"
    if isinstance(obj, dict):
        items = sorted((k, obj[k]) for k in obj if isinstance(k, str))
        return b"d" + b"".join(bencode(k) + bencode(v) for k, v in items) + b"e"


def bdecode(byt):
    return sdecode(byt.decode(encoding="utf-8"))[0]


def sdecode(stg):
    if stg[0].isdecimal():
        length, item = stg.split(":", maxsplit=1)
        return item[:int(length)], item[int(length):]
    if stg[0] == "i":
        end = stg.index("e")
        return int(stg[1:end]), stg[end+1:]
    if stg[0] in ("l", "d"):
        lst, t, stg = [], stg[0], stg[1:]
        while stg[0] != "e":
            item, stg = sdecode(stg)
            lst.append(item)
        seq = lst if t == "l" else {k: v for k, v in zip(lst[::2], lst[1::2])}
        return seq, stg[1:]