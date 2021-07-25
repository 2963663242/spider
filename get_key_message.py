import re
import decode
import ast
import html
import urllib.parse
def extract_map(js):
    key_map =  re.search(r"{\"[a-zA-Z0-9+=/]+\":.+\"}", js).group()
    key_map = key_map.replace("\/", "/")
    return  ast.literal_eval(key_map)
def get_base64s(js):
    return re.findall(r"\"[a-zA-Z0-9+=/]{100,}\"", js)
if __name__ == '__main__':
    with open("responese_text.txt", "r") as fp:
        js = fp.read()
    print(js)
    origin_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    key_map =extract_map(js)
    # key_map = key_map.replace("\/","/")
    # key_map = ast.literal_eval(key_map)
    print(key_map)
    first_decode = decode.decode_with_map(origin_str,key_map)
    print(first_decode)
    base64 = get_base64s(js)
    print("base64="+base64.__str__())
    base64_2 = decode.clear_speical_chars(base64[1])
    print("base64_2=" + base64_2)
    escape = decode.geteacape(base64_2,first_decode)
    print(escape)
    unescape = urllib.parse.unquote(escape)
    print(unescape)