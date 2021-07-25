import  re
def clear_speical_chars(str):
    p = re.compile('[^A-Za-z0-9+/=]')
    return p.sub("", str)
def decode_with_map(string,key_map):
    decode_str=""
    # for i in range(0,len(str)):
    for char in string:
        char = key_map.get(char,"")
        decode_str+=char
    return decode_str

def geteacape(a,key):
        b =""
        d = 0
        a = clear_speical_chars(a)
        if 64 == len(key):
                key += "="
        while True:
                a += ["", "===", "==", "="][len(a) % 4]
                if d >= len(a):
                        break
                e = key.find(a[d])
                d+=1
                c = key.find(a[d])
                d += 1
                f = key.find(a[d])
                d += 1
                g = key.find(a[d])
                d += 1
                e = (e << 2 | c >> 4),
                c = (c & 15) << 4 | f >> 2,
                h = (f & 3) << 6 | g,
                b += chr(e[0])
                if 64 != f:
                        b += chr(c[0])
                if 64 != g:
                        b += chr(h[0])
        return b


if __name__ == '__main__':
    # a = "TJEq+GofLgoPXdokVBCDV7EDVqIDV7TbTJEkTJTlTJEkLkokVdofXGokVBCDV7EDVyVDV7T8TJEkTJOmTJEkOkokVdokXkokV7aDV7EDVqIDV7T8TJEkTJTlTJEk+GokVdofXGokVy1DV7EDVyVDV7TVTJEkTJOmTJEk+GokVdokXkokVyIDV7EDVqIDV7TGTJEkTJTlTJEkodokVdofXGokVyIDV7EDVyVDV7T7TJEkTJOmTJEkLGokVdokXkokVyoDV7EDVqIDV7T7TJEkTJTlTJEkTJMlTJTSTJEkTJOmTJEkHdokVdokXkokVBhDV7EDVqIDV7EDOoVDVy+DV7EDVyVDV7EsTJEkTJOmTJEkZGokVdokXkokVDyDV7EDVqIDV7EsTJEkTJTlTJEkNGokVdofXGokVBUDV7EDVyVDV7T0TJEkTJOmTJEkNGokVdokXkokVvVDV7EDVqIDV7EqTJEkTJTlTJEkOgokVdofXGokVvVDV7EDVyVDV7TsTJEkTJOmTJEkJdokVdokXkokVyhDV7EDVqIDV7TsTJEkTJTlTJEkogokVdofXGokVBqDV7EDVyVDV7TxTJEkTJOmTJEkogokVdokXkokVDIDV7EDVqIDV7ToTJEkTJTlTJEkMgokVdofXGokVDIDV7EDVyVDV7TdTJEkTJOmTJEkokokVdokXkokVDVDV7EDVqIDV7TdTJEkTJTlTJEkHgokVdofXGokVy6DV7EDVyVDV7T3TJEkTJOmTJEkHgokVdokXkokVvyDV7EDVqIDV7TMTJEkTJTlTJEkMGokVdofXGokVvyDV7EDVyVDV7TnTJEkTJOmTJEkNgokVdokXkokV7CDV7EDVqIDV7TnTJEkTJTlTJEkagokVdofXGokVyEDV7EDVyVDV7TgTJEkTJOmTJEkagokVdokXkokVD+DV7EDVqIDV7EwTJEkTJTlTJEkOGokVdofXGokVD+DV7EDVyVDV7TwTJEkTJOmTJEkMkokVdokXkokVDaDV7EDVqIDV7TwTJEkTJTlTJEkGkokVdofXGokVBaDV7EDVyVDV7TvTJEkTJOmTJEkGkokVdokXkokVvIDV7EDVqIDV7TkTJEkTJTlTJEkadokVdofXGokVvIDV7EDVyVDV7TyTJEkTJOmTJEkGdokVdokXkokVyUDV7EDVqIDV7TyTJEkTJTlTJEkWdokVdofXGokVdokXdokVdokXkokVdokXdokVdofXGokVB+DV7EDVyVDV7TETJEkTJOmTJEkckokVdokXkokVB2DV7EDVqIDV7TETJEkTJTlTJEkLdokVdofXGokVvXDV7EDVyVDV7TqTJEkTJOmTJEkLdokVdokXkokVvaDV7EDVqIDV7EkTJEkTJTlTJEkVdokVdofXGokVvaDV7EDVyVDV7ThTJEkTJOmTJEkVGokVdokXkokV7IDV7EDVqIDV7ThTJEkTJTlTJEkVgokVdofXGokVyVDV7EDVyVDV7TlTJEkTJOmTJEkVgokVdokXkokVBoDV7EDVqIDV7TTTJEkTJTlTJEkGGokVdofXGokVBoDV7EDVyVDV7TATJEkTJOmTJEkZgokVdokXkokVDCDV7EDVqIDV7TATJEkTJTlTJEkZdokVdofXGokV7VDV7EDVyVDV7EfTJEkTJOmTJEkZdokVdokXkokVyqDV7EDVqIDV7TITJEkTJTlTJEkLgokVdofXGokVyqDV7EDOqXDVqEDV7L5TJE1TJOITJE1QshK+s92HgokNgoPXBOU+QTfTJOmTJE1TJEq+GoPLgokXkokVgokOSXDV7yDVqEDVIIDV7LDTJOIQsaDV7CDV7LDTJTlOloqNJEDV7yDVqEDVIIDV7LDTJOIQs1DV7CDV7LDTJErTJOgTJmmTJEqWGofL9FvTJEhTJEqWGokXfEkOJCfTJErTJOgTJmmTJEqWGofL9FvTJEhTJEqWGokXfowO7+kTJErTJOgTJmmTJEqWGofL9FvTJEhTJEqWGokXfEhVJVtTJErTJOgTJmmTJEqWGofL9FvTJEhTJEqWGokXfIhVJyfTJErTJOgTJmmTJmmTJEq+dokVgofLgokV9F5RBO4HS1DV7CDOqT5WQyDVqIDV7pDV7L5TJiITJTlTJE1TJEqWGokNGofXdo1XMFARBO4HS1DV7CDV7L7TJTlTJEq+kokXwFdTJEhQPIDV7CDV7LdTJErTJErTJErTJOg"
    # a.replace("/[^A-Za-z0-9\+\/\=]/g", "")
    # a ="TJE+=^^q+G///of&()*&^%*&L==goP"
    # a = clear_speical_chars(a)
    # print(a)
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    map =  {
            "x": "t",
            "t": "x",
            "5": "r",
            "r": "5",
            "Z": "W",
            "W": "Z",
            "h": "4",
            "4": "h",
            "/": "e",
            "e": "/",
            "I": "E",
            "E": "I",
            "m": "B",
            "B": "m",
            "k": "y",
            "y": "k",
            "Q": "X",
            "X": "Q",
            "1": "w",
            "w": "1",
            "7": "j",
            "j": "7",
            "l": "D",
            "D": "l",
            "K": "u",
            "u": "K",
            "A": "p",
            "p": "A",
            "n": "v",
            "v": "n",
            "2": "s",
            "s": "2",
            "d": "i",
            "i": "d",
            "N": "O",
            "O": "N",
            "J": "T",
            "T": "J",
            "3": "P",
            "P": "3",
            "c": "a",
            "a": "c",
            "g": "C",
            "C": "g",
            "G": "S",
            "S": "G",
            "L": "R",
            "R": "L",
            "9": "F",
            "F": "9",
            "6": "8",
            "8": "6",
            "M": "V",
            "V": "M",
            "H": "b",
            "b": "H",
            "+": "Y",
            "Y": "+",
            "o": "U",
            "U": "o",
            "q": "0",
            "0": "q",
            "z": "f",
            "f": "z"
        }
    decode_string = decode_with_map(string,map)
    print(decode_string)
