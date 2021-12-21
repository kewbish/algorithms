with open("input.txt") as x:
    p1, p2 = x.read().splitlines()
    p1 = int(p1[28:]) - 1
    p2 = int(p2[28:]) - 1

track = [x for x in range(1, 11)]
p1_score = 0
p2_score = 0
dice_state = 0


def roll():
    global dice_state
    steps = (dice_state) % 100 + 1
    dice_state += 1
    return steps


def step(p1_playing=True):
    global p1
    global p2
    global p1_score
    global p2_score
    total_steps = sum([roll(), roll(), roll()])
    new_pos = ((p1 if p1_playing else p2) + total_steps) % 10
    score = track[new_pos]
    if p1_playing:
        p1_score += score
        p1 = new_pos
    elif not p1_playing:
        p2_score += score
        p2 = new_pos


game_index = 1
while p1_score < 1000 and p2_score < 1000:
    step(game_index % 2)
    game_index += 1

print(min(p1_score, p2_score) * dice_state)
