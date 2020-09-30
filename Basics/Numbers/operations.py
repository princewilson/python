def reverse(a):
    rev = ''
    while a > 0:
        rem = a % 10
        rev = rev + str(rem)
        a = a // 10
    rev = int(rev)
    return rev

def toBinary(a):
    bins = ''
    while a > 0:
        rem = a % 2
        bins = bins + str(rem)
        a = a // 2
    bins2 = ''
    for i in range(len(bins)):
        bins2 = bins2 + bins[len(bins) - 1 - i]
    bins2 = int(bins2)
    return bins2
