def nonDivisibleSubset(k, s):
    if k == 0 or k == 1:
        return 1
    else:
        tempS  = [i%k for i in s]
        remainders = tempS.copy()
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if remainders[i] + remainders[j] == k:
                    if remainders.count(remainders[i]) == remainders.count(remainders[j]):
                        if remainders[i] in tempS:
                            tempS.remove(remainders[i])
                    else:
                        if remainders.count(remainders[i]) > remainders.count(remainders[j]):
                            if remainders[j] in tempS:
                                tempS.remove(remainders[j])
                        elif remainders.count(remainders[j]) > remainders.count(remainders[i]):
                            if remainders[i] in tempS:
                                tempS.remove(remainders[i])
        return len(tempS)

print(nonDivisibleSubset(4,[19,10,12,10,24,25,22]) )
