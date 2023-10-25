# int b: the number of black gifts
# int w: the number of white gifts
# int bc: the cost of a black gift
# int wc: the cost of a white gift
# int z: the cost to convert one color gift to the other color
def taumBday(b,w,bc,wc,z):
    
    if (bc+z <= wc):# check if is better to transform black to white
        return bc*b + ((bc+z) * w)
    elif (wc+z <= bc):# check if is better to transform white to black
        return ( (wc+z) * b) + (wc* w)
    else:
        return bc*b + wc*w



print(taumBday(5,5,2,3,4) )