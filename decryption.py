rec = ""
rec = input("What you want to decrypt: ")
rec.lower()
i = 0
while(i<len(rec)):
    if rec[i] == '3':
        print(",", end="")
    if rec[i] == '@':
        print(".", end="")
    if rec[i] == '1':
        print("!", end="")
    if rec[i] == '2':
        print("?", end="")
    if rec[i] == ' ':
        print(" ", end="")
    if rec[i] == '~':
        print("a", end="")
    if rec[i] == '!':
        print("b", end="")
    if rec[i] == '#':
        print("c", end="")
    if rec[i] == '$':
        print("d", end="")
    if rec[i] == '%':
        print("%e", end="")
    if rec[i] == '^':
        print("f", end="")
    if rec[i] == '&':
        print("g", end="")
    if rec[i] == '*':
        print("h", end="")
    if rec[i] == '(':
        print("i", end="")
    if rec[i] == ')':
        print("j", end="")
    if rec[i] == '_':
        print("k", end="")
    if rec[i] == '+':
        print("l", end="")
    if rec[i] == '/':
        print("m", end="")
    if rec[i] == '|':
        print("n", end="")
    if rec[i] == '-':
        print("o", end="")
    if rec[i] == ';':
        print("p", end="")
    if rec[i] == ':':
        print("q", end="")
    if rec[i] == '`':
        print("r", end="")
    if rec[i] == ',':
        print("s", end="")
    if rec[i] == '.':
        print("t", end="")
    if rec[i] == '>':
        print("u", end="")
    if rec[i] == '<':
        print("v", end="")
    if rec[i] == '}':
        print("w", end="")
    if rec[i] == '{':
        print("x", end="")
    if rec[i] == ']':
        print("y", end="")
    if rec[i] == '[':
        print("z", end="")
    
    i+=1
