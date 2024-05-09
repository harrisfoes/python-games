def to_celsius(f):
    return 5/9 * (f - 32)


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees farenheight is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)

