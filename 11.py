while True:
    s = input('>')
    if not s: break

    b = s.find('h')
    e = s.rfind('h')

    print(s[:b] + s[e + (e != -1):])