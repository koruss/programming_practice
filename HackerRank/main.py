# def breakingRecords(scores):
#     initial = scores.pop(0)
#     worst:int = initial
#     best:int = initial
#     bestCount:int = 0
#     worstCount:int = 0
    
#     for i in scores:

#         if i > best:
#             best = i
#             bestCount +=1
#         elif i < worst:
#             worst = i
#             worstCount +=1

#     print(bestCount, worstCount)
#     return [bestCount, worstCount] if bestCount > worstCount else [worstCount, bestCount]


# breakingRecords([3,4,21,36,10,28,35,5,24,42])

# def checker(s:[int],d:int,m:int):
#     count = 0
#     for i in range(m):
#         count = count + s[i]
#     return True if count ==d else False
        

# def funcion(s:[int],d:int,m:int):
#     count = 0
#     for i in range(len(s)-m + 1):
#         if checker(s[i:],d,m):
#             count +=1


#     print(count)
#     return count




# funcion([1,1,1,1,1,1],3,2)


# def divisibleSumPairs(n:int, k:int, ar:[int]):
#     count:int = 0
#     for i in range(n):
#         for j in range(n):
#             if i < j and (ar[i] + ar[j]) % k == 0:
#                 count +=1
#     print(count)
#     return count

# divisibleSumPairs(6,3,[1,3,2,6,1,2])


def timeConversion(s:str):
    newTime = ""
    time = s[0:2]
    if "AM" in s:
        if time == "12":
            newTime = "00" + s[2:-2]
        else:
            newTime = s[:-2]
    elif "PM" in s:
        if time == "12":
            newTime = time + s[2:-2]
        else:
            
            newTime = str(abs(int(time) + 12)) + s[2:-2]

    return newTime

timeConversion("12:59:59AM")
