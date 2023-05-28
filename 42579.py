# 42579
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_total = defaultdict(int)
    genre_dic = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total[genre] += play
        genre_dic[genre].append((play, i))
    genre_total = dict(sorted(genre_total.items(), key=lambda items: items[1], reverse=True))

    for genre in genre_total.keys():
        songs = sorted(genre_dic[genre], key=lambda x: x[1])
        print(sorted(songs, key=lambda x: x[0], reverse=True))
        for best_song in sorted(songs, key=lambda x: x[0], reverse=True)[:2]:
            answer.append(best_song[1])

    return answer


g1 = ["classic", "pop", "classic", "classic", "pop"]
p1 = [500, 600, 150, 800, 2500]
g = ["classic", "classic", "classic"]
p = [2500, 800, 2500]

print(solution(g, p))
print(solution(g1, p1))
