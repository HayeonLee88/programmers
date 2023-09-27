# 12946: 하노이의 탑

def solution(n):
    '''

    :param
        n: number of disks
        return: list of all start and end positions during hanoi algorithm
    '''
    def hanoi_move(num, start, end, via):
        '''
        하노이 탑 알고리즘에 따라 원판 옯기기
        :params
            num: total number of disks
            tart: start position
            end: end position
            via: via position

        '''
        if num <= 1:
            answer.append([start, end]) # 옮겨야 할 원판이 1개이면 원판을 옮기는 위치 저장
            return True
        # n - 1개의 원판을 보조 기둥으로 이동하기
        hanoi_move(num - 1, start, via, end)
        answer.append([start, end]) # 시작 기둥에서 마지막 원판이 남았을 때 옮기는 위치 저장
        # 보조 기둥에 있는 n - 1개의 원판을 도착 기둥으로 이동하기
        hanoi_move(num - 1, via, end, start)
        return True

    answer = []
    hanoi_move(n, 1, 3, 2)

    return answer