string = input().rstrip()

for c in string:
    if 'A'<=c<='Z':
        print(c.lower(), end = "")
    else:
        print(c.upper(), end = "")