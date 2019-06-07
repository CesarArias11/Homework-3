

def equal(a, b, c):
    if int(a) == int(b) and int(b) == int(c) and int(c) == int(a):
        return True
    elif int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
        return True
    else:
        return False


print(equal("5", "5", "5"))

