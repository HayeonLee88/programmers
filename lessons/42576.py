# lessons/42576
def solution(participant, completion):
    try:
        answer = (set(participant) - set(completion)).pop()
    except KeyError:
        participant.sort()
        completion.sort()
        answer = participant.pop()
        for i in range(len(participant)):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
    return answer
p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
print(solution(p, c))