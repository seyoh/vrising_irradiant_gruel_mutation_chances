def calculateChanceOfSuccess(n):
    known_chances = {0: 1, 1: 0.65, 2: 0.53625}
    for i in range(3, n + 1):
        chance = 0.325 * known_chances[i-1] + 0.325 * known_chances[i-2]
        known_chances[i] = chance
    return known_chances[n]

#Older complicated version of the calcul
def calculateCUntilN(n):
    #C(n) = f(n) + f(n-1) * 0.325
    if n == 0:
        return 1
    elif n == 1:
        return 0.65
    elif n == 2:
        return 0.53625
    else:
        fpp, fp, f = calculateFUntilN(n)
        return f + fp * 0.325


def calculateFUntilN(n):
    f1 = 0.325
    f2 = 0.430625
    if n == 1:
        return None, None, f1
    elif n == 2:
        return None, f1, f2
    else:
        fpp = f1
        fp = f2
        for i in range(3, n + 1):
            f = calculateFFromPrevious(fpp, fp)
            if i != n:
                fpp = fp
                fp = f
        return fpp,fp,f

def calculateFFromPrevious(FpreviousPrevious, Fprevious):
    #f(n) = f(n-1) * 0.325 + f(n-2) * 0.325
    return Fprevious * 0.325 + FpreviousPrevious * 0.325


