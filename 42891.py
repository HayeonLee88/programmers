# 42891: 무지의 먹방 라이브
'''
먹어야 할 음식 N개, 각 음식에 매겨진 번호(1~N)
1. 1번부터 순서대로 먹기.
2. 마지막 번호를 먹은 후 다시 1번부터 먹기
3. 1초 동안 음식 섭취, 남은 음식을 두고 다음 음식(남아있는 가장 가까운 번호) 먹기
4. 음식이 바뀔 때 걸리는 시간은 0초
 problem: k초 후 먹어야 할 음식의 번호는?
 k초 후 남은 음식이 없을 경우 -1 리턴
 1 <= food_times <= 2000, 1<= 시간(원소) <=1000, 1<= k <= 2,000,000
 효율성: 1 <= food_times <= 200,000, 1<= 시간(원소) <=100,000,000, 1<= k <= 2*10^13

 각 음식은 음식의 시간만큼 턴이 돌면 사라짐. => 우선순위 큐 heapq 사용
 만약 힙큐에 들어온 제일 작은 시간이 1일 때 이 음식을 다 먹는데 걸리는 시간은: len(food_times)
 위의 음식을 다 먹은 후 남은 음식의 수는 len(food_times) - 1
 만약 다음 음식의 시간이 n이라면 이 음식을 다 먹은 후 걸린 시간은:
 len(food_times) + len(food_times) - 1 + ... + len(food_times)- 1 -> len(food_times) + (len(food_times) - 1) * (n - 1)
 첫 음식을 다 먹은 후 다음 음식을 다 먹는 시간은 => (len(food_times) - 1) * (n - 1)
 남은 음식 개수는 len(food_times) - 2
 k가 현재 음식을 다 먹을 때까지 걸리는 시간보다 작으면 break => 음식 번호 순으로 정렬한 heapq[k % (남은 음식 개수)]
'''
import heapq

def solution(food_times, k):
    length = len(food_times)
    if sum(food_times) <= k:
        return -1
    h = []
    for i, time in enumerate(food_times):
        heapq.heappush(h, (time, i + 1))
    sum_time = 0
    pre_time = 0
    while sum_time + (h[0][0] - pre_time) * length <= k: # 현재 음식까지 먹는데 걸리는 시간이 k보다 작거나 같을 동안
        now = heapq.heappop(h)[0] # 먹는 시간이 작은 순으로 pop
        sum_time += (now - pre_time) * length # 현재 음식을 다 먹는데 걸리는 시간을 합한다
        length -= 1 # 음식의 개수
        pre_time = now
    result = sorted(h, key=lambda x: x[1]) # 남은 음식의 인덱스 순으로 정렬하기
    return result[k % length][1]
print(solution([3, 1, 2], 5))