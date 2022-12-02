with open("input.txt") as x:
    games = x.readlines()

score = 0
for game in games:
    them, you = game.strip().split(" ")
    if you == "X":
        if them == "A":
            score += 3
        elif them == "B":
            score += 1
        else:
            score += 2
    elif you == "Y":
        if them == "A":
            score += 1
        elif them == "B":
            score += 2
        else:
            score += 3
        score += 3
    elif you == "Z":
        if them == "A":
            score += 2
        elif them == "B":
            score += 3
        else:
            score += 1
        score += 6

print(score)
