def lz78(charstream, verbose=False):

    dict = {}
    p = ""
    code = []
    i = 0
    while True:
        c = charstream[i]
        try:
            dict[p + c]
            p = p + c
        except (KeyError):
            if p == "":
                o = 0
            else:
                o = dict[p]
            code.append((o, c))
            dict[p + c] = len(dict) + 1
            p = ""
        i += 1
        if i < len(charstream):
            continue
        else:
            if p != "":
                code.append((dict[p], "EOF"))
            break
    output = ""
    for block in code:
        for part in block:
            output += str(part)
    print(output)
    print(code)

lz78('Lorem ipsum dolor sit amet consectetur adipiscing elit proin ac lectus laoreet bibendum diam sit amet ullamcorper purus fusce sodales')