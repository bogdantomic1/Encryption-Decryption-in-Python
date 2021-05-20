rec = ""
rec = input("What you want to encrypt: ")
rec.lower()
i = 0
while(i<len(rec)):
    if rec[i] == ',':
        print("3", end="")
    if rec[i] == '.':
        print("@", end="")
    if rec[i] == '!':
        print("1", end="")
    if rec[i] == '?':
        print("2", end="")
    if rec[i] == ' ':
        print(" ", end="")
    if rec[i] == 'a':
        print("~", end="")
    if rec[i] == 'b':
        print("!", end="")
    if rec[i] == 'c':
        print("#", end="")
    if rec[i] == 'd':
        print("$", end="")
    if rec[i] == 'e':
        print("%", end="")
    if rec[i] == 'f':
        print("^", end="")
    if rec[i] == 'g':
        print("&", end="")
    if rec[i] == 'h':
        print("*", end="")
    if rec[i] == 'i':
        print("(", end="")
    if rec[i] == 'j':
        print(")", end="")
    if rec[i] == 'k':
        print("_", end="")
    if rec[i] == 'l':
        print("+", end="")
    if rec[i] == 'm':
        print("/", end="")
    if rec[i] == 'n':
        print("|", end="")
    if rec[i] == 'o':
        print("-", end="")
    if rec[i] == 'p':
        print(";", end="")
    if rec[i] == 'q':
        print(":", end="")
    if rec[i] == 'r':
        print("`", end="")
    if rec[i] == 's':
        print(",", end="")
    if rec[i] == 't':
        print(".", end="")
    if rec[i] == 'u':
        print(">", end="")
    if rec[i] == 'v':
        print("<", end="")
    if rec[i] == 'w':
        print("}", end="")
    if rec[i] == 'x':
        print("{", end="")
    if rec[i] == 'y':
        print("]", end="")
    if rec[i] == 'z':
        print("[", end="")
    i+=1

