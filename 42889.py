# 42889번: 실패율
'''
통과하지 못한 스테이지 리스트를 오름차순 정렬
스테이지 리스트를 순차적으로 탐색하여 현재 스테이지가 이전 스테이지를 통과했는지 확인
이전 스테이지의 실패율 = cnt / total
total = total - 이전 스테이지 개수
'''
def solution(N, stages):
    answer = [[i, 0] for i in range(1, N + 1)]
    total = len(stages)
    stages.sort()
    cnt = 0
    pre = stages[0] # 해당 스테이지를 통과한 사람을 체크하기 위한 변수
    for stage in stages:
        if stage > N: # 모든 스테이지를 통과한 사람 맨 끝
            break
        if stage != pre: # 이전 스테이지를 통과했을 경우
            answer[pre-1][1] = cnt / total
            total -= cnt
            cnt = 0
            pre = stage
        cnt += 1
    if cnt != 0: # 스테이지를 통과하지 못한 번호로 끝날 때
        answer[pre - 1][1] = cnt / total

    answer.sort(key=lambda x: x[0]) # 스테이지 번호를 기준으로 오름차순 전렬
    answer.sort(reverse=True, key=lambda x: x[1]) # 실패율을 기준으로 내림차순 정렬
    dic = dict(answer)
    # 스테이지(키)를 리스트로 변환하여 리턴
    return list(dic.keys())

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

s2 = [4,4,4,4,4]
print(solution(n, stages))
print(solution(4, s2))