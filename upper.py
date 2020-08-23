a = input()
if len(a) > 1:
    if a[:].isupper():
        print(a.lower())
    elif a[0].islower() | a[1:].isupper():
        a = a[0].upper()+a[1:].lower()
        print(a)
    else:
        print(a)
else:
    print(a)
