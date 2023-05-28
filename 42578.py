# 42578
from functools import reduce

def solution(clothes):
    closet = {}
    for clothe in clothes:
        type = clothe[1]
        if type in closet.keys():
            closet[type] += 1
        else:
            closet[type] = 2
    answer = reduce(lambda x, y: x * y, closet.values()) - 1
    return answer


data = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(data))
