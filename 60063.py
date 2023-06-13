'''
60063: 블록 이동하기
NxN 크기의 블록 내에서 2x1 크기의 로봇이 상, 하, 좌, 우 이동 & 로봇의 한 쪽을 축으로 회전한다.
로봇이 이동하거나 회전할 때 걸리는 시간은 1
로봇은 처음에 (1, 1) (1, 2) 칸에 있으며 로봇이 이동/회전하여 로봇이 차지하는 두 칸 중 한 칸이 (N, N)에 도착하면 멈춘다.
problem: 이때 걸리는 최소한의 시간을 구하여라.

    로봇의 회전
        -로봇이 가로로 위치할 때:
            로봇의 바로 위 두 칸이 비어 있으면 로봇은 한 축을 기준으로 시계/반시계방향으로 90도 회전할 수 있다.
            > 왼쪽을 축으로 반시계방향 90도 회전, 오른쪽을 축으로 시계방향 90도 회전
            로봇의 바로 아래 두 칸이 비어 있으면 로봇은 한 축을 기준으로 시계/반시계방향으로 90도 회전할 수 있다.
            > 왼쪽을 축으로 시계방향 90도 회전, 오른쪽을 축으로 반시계방향 90도 회전

        -로봇이 세로로 위치할 때:
            로봇의 바로 왼쪽 두 칸이 비어 있으면 로봇은 한 축을 기준으로 시계/반시계방향으로 90도 회전할 수 있다.
            > 위쪽을 축으로 시계방향 90도 회전, 아래쪽을 축으로 반시계방향 90도 회전
            로봇의 바로 오른쪽 두 칸이 비어 있으면 로봇은 한 축을 기준으로 시계/반시계방향으로 90도 회전할 수 있다.
            > 위쪽을 축으로 반시계방향 90도 회전, 아래쪽을 축으로 시계방향 90도 회전
'''
from collections import deque

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for i in range(n + 2)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_board[i][j] = board[i - 1][j - 1]

    # 상, 하, 좌, 우 이동 방향 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 로봇의 이동/회전으로 새로운 위치를 얻는 함수
    def get_new_pos(pos, board):
        pos = list(pos) # 사전을 리스트화
        new_pos = [] # 새로운 위치를 담을 리스트
        pos1, pos2 = pos
        pos1_x, pos1_y = pos1
        pos2_x, pos2_y = pos2

        for i in range(4):  # 상, 하, 좌, 우 이동
            n_pos_x1 = pos1_x + dx[i]
            n_pos_y1 = pos1_y + dy[i]
            n_pos_x2 = pos2_x + dx[i]
            n_pos_y2 = pos2_y + dy[i]
            if board[n_pos_x1][n_pos_y1] == 0 and board[n_pos_x2][n_pos_y2] == 0: # 이동할 칸이 비어 있다면
                new_pos.append({(n_pos_x1, n_pos_y1), (n_pos_x2, n_pos_y2)})

        if pos1_x == pos2_x:  # 로봇이 가로일 때
            for i in [-1, 1]:
                # 로봇의 위/아래 칸이 모두 비어 있다면
                if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                    new_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                    new_pos.append({(pos2_x + i, pos2_y), (pos2_x, pos2_y)})
        else:  # 로봇이 세로일 때
            for i in [-1, 1]:
                # 로봇의 양/옆 칸이 모두 비어 있다면
                if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                    new_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                    new_pos.append({(pos2_x, pos2_y + i), (pos2_x, pos2_y)})

        return new_pos

    visited = []
    pos = {(1, 1), (1, 2)} # 로봇의 시작 위치
    q = deque()
    q.append((pos, 0)) # 로봇의 위치와 걸리는 시간을 담는다
    while q:
        pos, cnt = q.popleft()
        if (n, n) in pos: # 로봇이 (n, n)칸에 도착하면
            return cnt

        for n_pos in get_new_pos(pos, new_board):
            if n_pos not in visited: # 새로 이동한 곳을 방문한 적이 없다면
                visited.append(n_pos)
                q.append((n_pos, cnt + 1))

#b = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

b = [[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 0], [0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0]]

print(solution(b))
