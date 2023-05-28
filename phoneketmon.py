# 해시: 폰켓몬
def solution(nums):
    set_nums = set(nums)
    choose_num = len(nums) // 2
    monster_types = len(set_nums)
    if choose_num < monster_types:
        return choose_num
    else:
        return monster_types
