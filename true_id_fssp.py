

def true_id(a, b):
    if len(a) + len(b) > 4:
        return a + b
    sym = '0' * (4 - len(a) - len(b))
    return a + sym + b

print(true_id('1', '2'))
print(true_id('1', '78'))
print(true_id('22', '33'))
print(true_id('45', '1'))
print(true_id('45', '145'))
print(true_id('453', '145'))