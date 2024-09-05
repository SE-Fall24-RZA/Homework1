import math
def powOfTwo(x):
    result = math.ceil(math.log2(x)) - math.floor(math.log2(x))
    if result == 0:
        return True
    else:
        return False
#print(powOfThree(17))