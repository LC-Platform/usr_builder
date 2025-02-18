from wxconv import WXC

def devanagari_to_wx(word):
    wxc = WXC()
    return wxc.convert(word)

