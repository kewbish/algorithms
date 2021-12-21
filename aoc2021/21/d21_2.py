from functools import cache

with open("input.txt") as x:
    p1, p2 = x.read().splitlines()
    p1 = int(p1[28:]) - 1
    p2 = int(p2[28:]) - 1


track = [x for x in range(1, 11)]
p1_score = 0
p2_score = 0

# toys r us getting real fancy huh
@cache
def count_wins_from(p1, p2, p1_score, p2_score):
    if p1_score >= 21:
        return (1, 0)
    elif p2_score >= 21:
        return (0, 1)
    ans = (0, 0)
    for dice_1 in range(1, 4):
        for dice_2 in range(1, 4):
            for dice_3 in range(1, 4):
                new_player = (p1 + dice_1 + dice_2 + dice_3) % 10
                new_score = p1_score + track[new_player]
                p1_wins, p2_wins = count_wins_from(p2, new_player, p2_score, new_score)
                ans = (ans[0] + p2_wins, ans[1] + p1_wins)
    return ans


print(max(count_wins_from(p1, p2, p1_score, p2_score)))
