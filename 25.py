import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
brojevi = []

def convert(x):
    ls = reversed(x)
    coef = 1
    rv = 0
    for i in ls:
        if i == '-':
            rv -= coef
        elif i == '=':
            rv -= 2*coef
        else:
            rv += int(i) * coef
        coef *= 5
    return rv

def convert2(x):
    rv = ""
    prijenos = 0
    while x != 0:
        if x % 5 == 0:
            if prijenos == 1:
                rv += '1'
                prijenos = 0
            else:
                rv += '0'
        elif x % 5 == 1:
            if prijenos == 1:
                rv += '2'
                prijenos = 0
            else:
                rv += '1'
        elif x % 5 == 2:
            if prijenos == 1:
                rv += '='
                prijenos = 1
            else:
                rv += '2'
        elif x % 5 == 3:
            if prijenos == 1:
                rv += '-'
                prijenos = 1
            else:
                rv += '='
                prijenos = 1
        elif x % 5 == 4:
            if prijenos == 1:
                rv += '0'
                prijenos = 1
            else:
                rv += '-'
                prijenos = 1
        x //= 5
    if prijenos == 1:
        rv += '1'
    return rv[::-1]

brojevi = map (convert , lines)
sm = sum(brojevi)
outt = convert2(sm)
print(outt)

