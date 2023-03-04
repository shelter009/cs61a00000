import random
result = []
def avanage_score(count):

    if count < 15:
        return result.append(count) 
    else:
        a = random.randint(15,20)
        return result.append(avanage_score(count - a))
avanage_score(100)
print(result)