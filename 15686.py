# 15686번: 치킨 배달
'''
NxN 크기 도시: 각 칸은 빈 칸(0), 치킨집(2), 집(1)
칸: (r, c) 원소는 1부터 시작
치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리 (집 기준으로)
도시의 치킨 거리 = 모든 집의 치킨 거리의 합
두 칸 사이의 거리 = |r1 - r2| + |c1 - c2|
치킨집 중 최대 M개를 골라 도시의 치킨 거리를 가장 작게 만들어라.
2 ≤ N ≤ 50, 1 ≤ M ≤ 13, 1 <= 집의 개수 <= 2N, M <= 치킨집의 개수 <= 13
치킵집 조합 최대 13C6 = 약 1700
1700 * 100 * 13 = 약 1,700,000 => brute force로 풀기
'''
from itertools import combinations
n, m = map(int, input().split())
chickens = [] # 치킨집의 좌표를 담는 리스트
houses = [] # 집의 좌표를 담는 리스트
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        x = row[j - 1]
        if x == 2:
            chickens.append((i, j))
        elif x == 1:
            houses.append((i, j))

distances = [] # 길이가 치킨집 개수인 각 치킨집과 모든 집 사이의 거리를 담는 리스트
for chicken in chickens:
    tmp = []
    for house in houses:
        tmp.append(abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]))
    distances.append(tmp)
# 치킨집 중 m개를 뽑아 리스트로 만들기
pick_chicken = list(combinations(distances, m))

# 도시의 치킨 거리
city_dist = []
for picked in pick_chicken:
    tmp = 0
    for i in range(len(houses)):
        min_dist = 100 # 각 집의 치킨 거리
        for j in range(m):
            min_dist = min(min_dist, picked[j][i])
        tmp += min_dist
    city_dist.append(tmp)
print(min(city_dist))