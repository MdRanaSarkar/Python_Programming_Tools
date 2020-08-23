def checkoddoreven(n):
    if n & 1 == 0:
        print("Even")
    else:
        print("odd")


# for test case
t = int(input())
while t:
    number = int(input())
    checkoddoreven(number)
