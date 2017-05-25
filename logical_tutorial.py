for num in range(30,301):
    if num % 7 == 0 and num % 13 == 0:
        msg = "a-z"
    elif num % 13 == 0:
        msg = "xyz"
    elif num % 7 == 0:
        msg = "abc"
    else:
        msg = str(num)
    print (msg)
