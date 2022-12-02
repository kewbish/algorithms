with open("input.txt") as x:
    games = x.readlines()

score = 0
for game in games:
    them, you = game.strip().split(" ")
    if you == "X":
        score += 1
    elif you == "Y":
        score += 2
    elif you == "Z":
        score += 3
    if (them == "A" and you == "Y") or (them == "B" and you == "Z") or (them == "C" and you == "X"):
        score += 6
    elif (them == "A" and you == "X") or (them == "B" and you == "Y") or (them == "C" and you == "Z"):
        score += 3

print(score)
